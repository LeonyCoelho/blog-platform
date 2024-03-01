from django.contrib import admin
from django.urls import include, path
from app_blog_platform import views
from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [
    path('admin/', admin.site.urls),



    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('view_post/<int:post_id>/', views.view_post, name='view_post'),

    path('posts/tag_1/<int:tag_id>/', views.post_list_by_tag_1, name='post_list_by_tag_1'),
    path('posts/tag_2/<int:tag_id>/', views.post_list_by_tag_2, name='post_list_by_tag_2'),
    path('posts/tag_3/<int:tag_id>/', views.post_list_by_tag_3, name='post_list_by_tag_3'),

    path('settings/list_posts/', views.list_posts, name='list_posts'),
    path('settings/new_post/', views.new_post, name='new_post'),
    path('settings/edit_about/', views.edit_about, name='edit_about'),
    path('settings/edit_home/', views.edit_home, name='edit_home'),
    path('settings/edit_global_settings/', views.edit_global_settings, name='edit_global_settings'),
    path('settings/edit_bg/', views.edit_bg, name='edit_bg'),
    path('settings/toggle_use_image/', views.toggle_use_image, name='toggle_use_image'),

    path('settings/general_settings/', views.settings, name='settings'),
    path('create_tag_1/', views.create_tag_1, name='create_tag_1'),
    path('create_tag_2/', views.create_tag_2, name='create_tag_2'),
    path('create_tag_3/', views.create_tag_3, name='create_tag_3'),

    path('autocomplete_tags_level_2/', views.autocomplete_tags_level_2, name='autocomplete_tags_level_2'),
    path('autocomplete_tags_level_3/', views.autocomplete_tags_level_3, name='autocomplete_tags_level_3'),

    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('get_tags_level_2/', views.get_tags_level_2, name='get_tags_level_2'),
    path('get_tags_level_3/', views.get_tags_level_3, name='get_tags_level_3'),
    path('search/', views.search_posts, name='search_posts'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)