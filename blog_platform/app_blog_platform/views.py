from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.http import JsonResponse
from django.views.decorators.http import require_GET
from django.shortcuts import render
from django.shortcuts import redirect
from django.db.models import Q


from .models import Post, Post_Slide_Images,Tags_Level_1 ,Tags_Level_2, Tags_Level_3

######################################
#
#                                       POSTS ADMIN FUNCITONS
#

def new_post(request):
    if request.method == 'POST':
        post_name = request.POST.get('post_name')
        post_body = request.POST.get('post_body')
        post_main_link_title = request.POST.get('post_main_link_title')
        post_main_link = request.POST.get('post_main_link')

        # Criar uma nova instância do Post
        new_post_instance = Post.objects.create(
            post_name=post_name,
            post_body=post_body,
            post_main_link=post_main_link,
            post_main_link_title=post_main_link_title
        )

        # Adicionar tags de nível 1 ao post, se existirem
        tags_level_1_ids = request.POST.getlist('post_tag_level_1')
        new_post_instance.post_tag_level_1.set(tags_level_1_ids)

        # Adicionar tags de nível 2 ao post, se existirem
        tags_level_2_ids = request.POST.getlist('post_tag_level_2')
        new_post_instance.post_tag_level_2.set(tags_level_2_ids)

        # Adicionar tags de nível 3 ao post, se existirem
        tags_level_3_ids = request.POST.getlist('post_tag_level_3')
        new_post_instance.post_tag_level_3.set(tags_level_3_ids)

        # Adicionar imagens ao post, se existirem
        images = request.FILES.getlist('post_slide_images')
        for image in images:
            post_slide_image = Post_Slide_Images.objects.create(post_slide_image=image)
            new_post_instance.post_slide_images.add(post_slide_image)

        return redirect('new_post')  # Substitua pelo nome correto da sua URL

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
    tags_level_1 = Tags_Level_1.objects.all()
    tags_level_2 = Tags_Level_2.objects.all()
    tags_level_3 = Tags_Level_3.objects.all()

    posts = Post.objects.all()

    context={
        'tags_level_1':tags_level_1,
        'tags_level_2':tags_level_2,
        'tags_level_3':tags_level_3,
        'posts':posts,
    }
    return render(request, 'list_posts.html', context)

def view_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'view_post.html', {'post': post})




def get_tag(request, tag_id):
    
    return redirect('post_list_by_tag_1')

def post_list_by_tag_1(request, tag_id):
    tag = get_object_or_404(Tags_Level_1, id=tag_id)
    posts = Post.objects.filter(post_tag_level_1__id=tag_id)
    return render(request, 'post_list_by_tag.html', {'tag': tag, 'posts': posts})


def post_list_by_tag_2(request, tag_id):
    tag = get_object_or_404(Tags_Level_2, id=tag_id)
    posts = Post.objects.filter(post_tag_level_2__id=tag_id)
    return render(request, 'post_list_by_tag.html', {'tag': tag, 'posts': posts})


def post_list_by_tag_3(request, tag_id):
    tag = get_object_or_404(Tags_Level_3, id=tag_id)
    posts = Post.objects.filter(post_tag_level_3__id=tag_id)
    return render(request, 'post_list_by_tag.html', {'tag': tag, 'posts': posts})



####################################
#
#                             SETTINGS
#

def settings(request):
    tags_level_1 = Tags_Level_1.objects.all()
    tags_level_2 = Tags_Level_2.objects.all()
    tags_level_3 = Tags_Level_3.objects.all()

    context = {
        'tags_level_1': tags_level_1,
        'tags_level_2': tags_level_2,
        'tags_level_3': tags_level_3,
    }
    return render(request, 'settings.html', context)


def create_tag_1(request):
    if request.method == 'POST':
        tag_name = request.POST.get('tag_name1')
        Tags_Level_1.objects.create(tag_name=tag_name)

    return redirect(reverse('settings'))

def create_tag_2(request):
    if request.method == 'POST':
        tag_name = request.POST.get('tag_name2')
        parent_tag_id = request.POST.get('parent_tag')

        # Retrieve the Tags_Level_1 instance based on the parent_tag_id
        try:
            parent_tag = Tags_Level_1.objects.get(id=parent_tag_id)
        except Tags_Level_1.DoesNotExist:
            # Handle the case where the Tags_Level_1 instance is not found
            # (You may want to add proper error handling or redirect to an error page)
            return redirect(reverse('settings'))

        # Create Tags_Level_2 with the association to Tags_Level_1
        new_tag_level_2 = Tags_Level_2.objects.create(tag_name=tag_name)
        
        # Add the Tags_Level_1 instance to the ManyToMany field using .set()
        new_tag_level_2.parent_tag.set([parent_tag])

    return redirect(reverse('settings'))

def create_tag_3(request):
    if request.method == 'POST':
        tag_name = request.POST.get('tag_name3')
        parent_tag_id = request.POST.get('parent_tag')

        # Retrieve the Tags_Level_1 instance based on the parent_tag_id
        try:
            parent_tag = Tags_Level_2.objects.get(id=parent_tag_id)
        except Tags_Level_2.DoesNotExist:
            # Handle the case where the Tags_Level_2 instance is not found
            # (You may want to add proper error handling or redirect to an error page)
            return redirect(reverse('settings'))

        # Create Tags_Level_3 with the association to Tags_Level_2
        new_tag_level_3 = Tags_Level_3.objects.create(tag_name=tag_name)
        
        # Add the Tags_Level_2 instance to the ManyToMany field using .set()
        new_tag_level_3.parent_tag.set([parent_tag])

    return redirect(reverse('settings'))


##################################
#
#                  ULTILITY
#


from django.http import JsonResponse



def get_tags_level_2(request):
    tag_level_1_id = request.GET.get('tag_level_1_id')
    tags_level_2 = Tags_Level_2.objects.filter(parent_tag__id=tag_level_1_id)
    data = [{'id': tag.id, 'tag_name': tag.tag_name} for tag in tags_level_2]
    return JsonResponse(data, safe=False)

def get_tags_level_3(request):
    tag_level_2_id = request.GET.get('tag_level_2_id')
    tags_level_3 = Tags_Level_3.objects.filter(parent_tag__id=tag_level_2_id)
    data = [{'id': tag.id, 'tag_name': tag.tag_name} for tag in tags_level_3]
    return JsonResponse(data, safe=False)
