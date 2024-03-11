from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.http import JsonResponse
from django.views.decorators.http import require_GET
from django.shortcuts import render
from django.shortcuts import redirect
from django.db.models import Q
from django.core.paginator import Paginator
from django.views.decorators.http import require_POST
from django.utils import timezone




from .models import Page, Post, Post_Slide_Images,Tags_Level_1 ,Tags_Level_2, Tags_Level_3, About, Home, Home_Slide_Images, Theme, Global_Settings


######################################
#
#                                      USER ACCESSIBLE  PAGES
#


def home(request):
    home = Home.objects.first()
    post_list = Post.objects.all()
    items_per_page = 6
    paginator = Paginator(post_list, items_per_page)
    page = request.GET.get('page', 1)
    posts = paginator.get_page(page)
    context = {
        'home':home,
        'posts':posts,
        }
    return render(request, 'home.html', context)

def about(request):
    about = About.objects.first()
    context = {'about':about,}
    return render(request, 'about.html',context)

def view_page(request, page_id):
    page = get_object_or_404(Page, id=page_id)
    return render(request, 'view_page.html', {'page': page})

def view_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'view_post.html', {'post': post})

# =========== PAGE LIST BY TAG =================

def page_list_by_tag_2(request, tag_id):
    tag = get_object_or_404(Tags_Level_2, id=tag_id)
    pages_list = Page.objects.filter(page_tag_level_2__id=tag_id)
    items_per_page = 8
    paginator = Paginator(pages_list, items_per_page)
    page = request.GET.get('page', 1)
    pages = paginator.get_page(page)
    return render(request, 'page_list_by_tag.html', {'tag': tag, 'pages': pages})


def page_list_by_tag_3(request, tag_id):
    tag = get_object_or_404(Tags_Level_3, id=tag_id)
    pages_list = Page.objects.filter(page_tag_level_3__id=tag_id)
    items_per_page = 8
    paginator = Paginator(pages_list, items_per_page)
    page = request.GET.get('page', 1)
    pages = paginator.get_page(page)
    return render(request, 'page_list_by_tag.html', {'tag': tag, 'pages': pages})

# =========== POST LIST BY TAG =================

def post_list_by_tag_1(request, tag_id):
    tag = get_object_or_404(Tags_Level_1, id=tag_id)
    posts_list = Post.objects.filter(post_tag_level_1__id=tag_id)
    items_per_page = 8
    paginator = Paginator(posts_list, items_per_page)
    page = request.GET.get('page', 1)
    posts = paginator.get_page(page)
    return render(request, 'post_list_by_tag.html', {'tag': tag, 'posts': posts})


def post_list_by_tag_2(request, tag_id):
    tag = get_object_or_404(Tags_Level_2, id=tag_id)
    posts_list = Post.objects.filter(post_tag_level_2__id=tag_id)
    items_per_page = 8
    paginator = Paginator(posts_list, items_per_page)
    page = request.GET.get('page', 1)
    posts = paginator.get_page(page)
    return render(request, 'post_list_by_tag.html', {'tag': tag, 'posts': posts})


def post_list_by_tag_3(request, tag_id):
    tag = get_object_or_404(Tags_Level_3, id=tag_id)
    posts_list = Post.objects.filter(post_tag_level_3__id=tag_id)
    items_per_page = 8
    paginator = Paginator(posts_list, items_per_page)
    page = request.GET.get('page', 1)
    posts = paginator.get_page(page)
    return render(request, 'post_list_by_tag.html', {'tag': tag, 'posts': posts})

######################################
#
#                                       PAGE ADMIN FUNCITONS
#

def new_page(request):
    if request.method == 'POST':
        page_name = request.POST.get('page_name')
        page_body = request.POST.get('page_body')
        page_main_link_title = request.POST.get('page_main_link_title')
        page_main_link = request.POST.get('page_main_link')
        page_cover_image = request.FILES.get('page_cover_image')
        new_page_instance = Page.objects.create(
            page_name=page_name,
            page_body=page_body,
            page_main_link=page_main_link,
            page_main_link_title=page_main_link_title,
            page_cover_image=page_cover_image
        )
        tags_level_1_ids = request.POST.getlist('page_tag_level_1')
        new_page_instance.page_tag_level_1.set(tags_level_1_ids)
        tags_level_2_ids = request.POST.getlist('page_tag_level_2')
        new_page_instance.page_tag_level_2.set(tags_level_2_ids)
        tags_level_3_ids = request.POST.getlist('page_tag_level_3')
        new_page_instance.page_tag_level_3.set(tags_level_3_ids)
        images = request.FILES.getlist('page_slide_images')
        for image in images:
            page_slide_image = Post_Slide_Images.objects.create(page_slide_image=image)
            new_page_instance.page_slide_images.add(page_slide_image)
        page_date = request.POST.get('page_date')
        if page_date:
            new_page_instance.page_date = page_date
        else:
            new_page_instance.page_date = timezone.now()
        new_page_instance.save()
        return redirect('new_page') 
    tags_level_2 = Tags_Level_2.objects.all()
    tags_level_3 = Tags_Level_3.objects.all()
    return render(request, 'new_page.html', {'tags_level_2': tags_level_2, 'tags_level_3': tags_level_3})


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
        post_cover_image = request.FILES.get('post_cover_image')
        new_post_instance = Post.objects.create(
            post_name=post_name,
            post_body=post_body,
            post_main_link=post_main_link,
            post_main_link_title=post_main_link_title,
            post_cover_image=post_cover_image
        )
        tags_level_1_ids = request.POST.getlist('post_tag_level_1')
        new_post_instance.post_tag_level_1.set(tags_level_1_ids)
        tags_level_2_ids = request.POST.getlist('post_tag_level_2')
        new_post_instance.post_tag_level_2.set(tags_level_2_ids)
        tags_level_3_ids = request.POST.getlist('post_tag_level_3')
        new_post_instance.post_tag_level_3.set(tags_level_3_ids)
        images = request.FILES.getlist('post_slide_images')
        for image in images:
            post_slide_image = Post_Slide_Images.objects.create(post_slide_image=image)
            new_post_instance.post_slide_images.add(post_slide_image)
        post_date = request.POST.get('post_date')
        if post_date:
            new_post_instance.post_date = post_date
        else:
            new_post_instance.post_date = timezone.now()
        new_post_instance.save()
        return redirect('new_post') 
    tags_level_2 = Tags_Level_2.objects.all()
    tags_level_3 = Tags_Level_3.objects.all()
    return render(request, 'new_post.html', {'tags_level_2': tags_level_2, 'tags_level_3': tags_level_3})

def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    post.delete()
    return redirect('list_posts')

def delete_page(request, page_id):
    page = get_object_or_404(Page, id=page_id)
    page.delete()
    return redirect('list_pages')

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

def list_pages(request):
    tags_level_1 = Tags_Level_1.objects.all()
    tags_level_2 = Tags_Level_2.objects.all()
    tags_level_3 = Tags_Level_3.objects.all()

    pages = Page.objects.all()

    context={
        'tags_level_1':tags_level_1,
        'tags_level_2':tags_level_2,
        'tags_level_3':tags_level_3,
        'pages':pages,
    }
    return render(request, 'list_pages.html', context)

####################################
#
#                             SETTINGS
#

def settings(request):
    tags_level_1 = Tags_Level_1.objects.all()
    tags_level_2 = Tags_Level_2.objects.all()
    tags_level_3 = Tags_Level_3.objects.all()
    about = About.objects.first()
    home = Home.objects.first()
    themes = Theme.objects.all()

    context = {
        'tags_level_1': tags_level_1,
        'tags_level_2': tags_level_2,
        'tags_level_3': tags_level_3,
        'about':about,
        'home':home,
        'themes':themes,
    }
    return render(request, 'settings.html', context)

def edit_global_settings(request):
    global_settings, created = Global_Settings.objects.get_or_create()

    if request.method == 'POST':
        blog_name = request.POST.get('blog_name')
        theme_names = request.POST.getlist('theme')

        global_settings.blog_name = blog_name
        global_settings.save()
        global_settings.theme.clear()
        for theme_name in theme_names:
            theme, _ = Theme.objects.get_or_create(theme_name=theme_name)
            global_settings.theme.add(theme)

    return redirect('settings')

def edit_bg(request):
    global_settings, create = Global_Settings.objects.get_or_create()
    if request.method == 'POST':
        bg_image = request.FILES.get('bg_image')
        global_settings.bg_image = bg_image
        global_settings.save()
    return redirect('settings')

def remove_bg(request):
    Global_Settings.objects.all().update(bg_image='')
    return redirect('settings')

def edit_logo(request):
    global_settings, create = Global_Settings.objects.get_or_create()
    if request.method == 'POST':
        logo_image = request.FILES.get('logo_image')
        global_settings.logo_image = logo_image
        global_settings.save()
    return redirect('settings')

def remove_logo(request):
    Global_Settings.objects.all().update(logo_image='')
    return redirect('settings')


def edit_about(request):
    about, created = About.objects.get_or_create()
    if request.method == 'POST':
        about_text = request.POST.get('about_text')
        about_image = request.FILES.get('about_image')
        about.about_text = about_text
        about.about_image = about_image
        about.save()
    return redirect('settings')

def edit_home(request):
    home = Home.objects.first()

    # Cria uma instância de Home se não existir
    if home is None:
        home = Home.objects.create()

    if request.method == 'POST':
        # Limpa as imagens existentes
        home.home_slide.clear()

        images = request.FILES.getlist('home_slide_images')

        for image in images:
            home_slide_image = Home_Slide_Images.objects.create(home_slide_image=image)
            home.home_slide.add(home_slide_image)

    return redirect('settings')



def toggle_use_image(request):
    about, created = About.objects.get_or_create()
    about.use_image = not about.use_image  # Inverte o estado atual
    about.save()
    return redirect('settings')  # Redireciona de volta para a página de configurações


def create_tag_1(request):
    if request.method == 'POST':
        tag_name = request.POST.get('tag_name1')
        Tags_Level_1.objects.create(tag_name=tag_name)

    return redirect(reverse('settings'))

# def create_tag_2(request):
#     if request.method == 'POST':
#         tag_name = request.POST.get('tag_name2')
#         parent_tag_id = request.POST.get('parent_tag')

#         # Retrieve the Tags_Level_1 instance based on the parent_tag_id
#         try:
#             parent_tag = Tags_Level_1.objects.get(id=parent_tag_id)
#         except Tags_Level_1.DoesNotExist:
#             # Handle the case where the Tags_Level_1 instance is not found
#             # (You may want to add proper error handling or redirect to an error page)
#             return redirect(reverse('settings'))

#         # Create Tags_Level_2 with the association to Tags_Level_1
#         new_tag_level_2 = Tags_Level_2.objects.create(tag_name=tag_name)
        
#         # Add the Tags_Level_1 instance to the ManyToMany field using .set()
#         new_tag_level_2.parent_tag.set([parent_tag])

#     return redirect(reverse('settings'))

# def create_tag_3(request):
#     if request.method == 'POST':
#         tag_name = request.POST.get('tag_name3')
#         parent_tag_id = request.POST.get('parent_tag')

#         # Retrieve the Tags_Level_1 instance based on the parent_tag_id
#         try:
#             parent_tag = Tags_Level_2.objects.get(id=parent_tag_id)
#         except Tags_Level_2.DoesNotExist:
#             # Handle the case where the Tags_Level_2 instance is not found
#             # (You may want to add proper error handling or redirect to an error page)
#             return redirect(reverse('settings'))

#         # Create Tags_Level_3 with the association to Tags_Level_2
#         new_tag_level_3 = Tags_Level_3.objects.create(tag_name=tag_name)
        
#         # Add the Tags_Level_2 instance to the ManyToMany field using .set()
#         new_tag_level_3.parent_tag.set([parent_tag])

#     return redirect(reverse('settings'))


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
        
        # Add the Tags_Level_1 instance to the ForeignKey field
        new_tag_level_2.parent_tag = parent_tag
        new_tag_level_2.save()

    return redirect(reverse('settings'))

def create_tag_3(request):
    if request.method == 'POST':
        tag_name = request.POST.get('tag_name3')
        parent_tag_id = request.POST.get('parent_tag')

        # Retrieve the Tags_Level_2 instance based on the parent_tag_id
        try:
            parent_tag = Tags_Level_2.objects.get(id=parent_tag_id)
        except Tags_Level_2.DoesNotExist:
            # Handle the case where the Tags_Level_2 instance is not found
            # (You may want to add proper error handling or redirect to an error page)
            return redirect(reverse('settings'))

        # Create Tags_Level_3 with the association to Tags_Level_2
        new_tag_level_3 = Tags_Level_3.objects.create(tag_name=tag_name)
        
        # Add the Tags_Level_2 instance to the ForeignKey field
        new_tag_level_3.parent_tag = parent_tag
        new_tag_level_3.save()

    return redirect(reverse('settings'))


def delete_tag_1(request, tag_1):
        tag = get_object_or_404(Tags_Level_1, id=tag_1)
        print('Proceding to delete:', tag_1)
        tag.delete()
        return redirect('settings')

def delete_tag_2(request, tag_2):
        tag = get_object_or_404(Tags_Level_2, id=tag_2)
        print('Proceding to delete:', tag_2)
        tag.delete()
        return redirect('settings')

def delete_tag_3(request, tag_3):
        tag = get_object_or_404(Tags_Level_3, id=tag_3)
        print('Error on delete tag:', tag_3)
        tag.delete()
        return redirect('settings')





##################################
#
#                  ULTILITY
#


from django.http import JsonResponse


def search_posts(request):
    query = request.GET.get('query')
    
    if query:
        posts_list = Post.objects.filter(Q(post_name__icontains=query) | Q(post_body__icontains=query)).distinct()
        items_per_page = 6
        paginator = Paginator(posts_list, items_per_page)
        page = request.GET.get('page', 1)
        posts = paginator.get_page(page)

    else:
        posts = Post.objects.all()

    return render(request, 'search_results.html', {'query': query, 'posts': posts})


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
