from django.contrib import admin
from django.urls import include, path
from app_blog_platform import views
from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.new_post, name='new_post'),


    path('posts/tag_1/<int:tag_id>/', views.post_list_by_tag_1, name='post_list_by_tag_1'),
    path('posts/tag_2/<int:tag_id>/', views.post_list_by_tag_2, name='post_list_by_tag_2'),
    path('posts/tag_3/<int:tag_id>/', views.post_list_by_tag_3, name='post_list_by_tag_3'),


    path('list_posts/', views.list_posts, name='list_posts'),
    path('view_post/<int:post_id>/', views.view_post, name='view_post'),
    path('settings/', views.settings, name='settings'),
    path('create_tag_1/', views.create_tag_1, name='create_tag_1'),
    path('create_tag_2/', views.create_tag_2, name='create_tag_2'),
    path('create_tag_3/', views.create_tag_3, name='create_tag_3'),

    path('autocomplete_tags_level_2/', views.autocomplete_tags_level_2, name='autocomplete_tags_level_2'),
    path('autocomplete_tags_level_3/', views.autocomplete_tags_level_3, name='autocomplete_tags_level_3'),

    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('get_tags_level_2/', views.get_tags_level_2, name='get_tags_level_2'),
    path('get_tags_level_3/', views.get_tags_level_3, name='get_tags_level_3'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
