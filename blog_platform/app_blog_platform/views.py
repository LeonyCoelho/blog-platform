from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.http import require_GET
from .models import Post, Post_Slide_Images, Tags_Level_2, Tags_Level_3

def new_post(request):
    if request.method == 'POST':
        post_name = request.POST.get('post_name')
        post_body = request.POST.get('post_body')
        post_main_link = request.POST.get('post_main_link')

        # Criar uma nova instância do Post
        new_post_instance = Post.objects.create(
            post_name=post_name,
            post_body=post_body,
            post_main_link=post_main_link
        )

        # Adicionar tags de nível 2 ao post, se existirem
        tags_level_2_names = request.POST.get('post_tag_level_2').split(',')
        for tag_name in tags_level_2_names:
            tag_name = tag_name.strip()
            tag_level_2, created = Tags_Level_2.objects.get_or_create(tag_name=tag_name)
            new_post_instance.post_tag_level_2.add(tag_level_2)

        # Adicionar tags de nível 3 ao post, se existirem
        tags_level_3_names = request.POST.get('post_tag_level_3').split(',')
        for tag_name in tags_level_3_names:
            tag_name = tag_name.strip()
            tag_level_3, created = Tags_Level_3.objects.get_or_create(tag_name=tag_name)
            new_post_instance.post_tag_level_3.add(tag_level_3)

        # Adicionar imagens ao post, se existirem
        images = request.FILES.getlist('post_slide_images')
        for image in images:
            post_slide_image = Post_Slide_Images.objects.create(post_slide_image=image)
            new_post_instance.post_slide_images.add(post_slide_image)

        return redirect('list_post')  # Substitua pelo nome correto da sua URL

    # Obter todas as tags de nível 2 e 3 para exibir no formulário
    tags_level_2 = Tags_Level_2.objects.all()
    tags_level_3 = Tags_Level_3.objects.all()

    return render(request, 'new_post.html', {'tags_level_2': tags_level_2, 'tags_level_3': tags_level_3})


@require_GET
def autocomplete_tags_level_2(request):
    term = request.GET.get('term', '')
    tags_level_2 = Tags_Level_2.objects.filter(tag_name__icontains=term).values_list('tag_name', flat=True)
    return JsonResponse(list(tags_level_2), safe=False)

@require_GET
def autocomplete_tags_level_3(request):
    term = request.GET.get('term', '')
    tags_level_3 = Tags_Level_3.objects.filter(tag_name__icontains=term).values_list('tag_name', flat=True)
    return JsonResponse(list(tags_level_3), safe=False)

def list_posts(request):
    posts = Post.objects.all()
    return render(request, 'list_posts.html', {'posts': posts})

def view_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'view_post.html', {'post': post})