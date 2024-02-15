"""
URL configuration for blog_platform project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from app_blog_platform import views
from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.new_post, name='new_post'),

    path('list_posts/', views.list_posts, name='list_posts'),
    path('view_post/<int:post_id>/', views.view_post, name='view_post'),

    path('autocomplete_tags_level_2/', views.autocomplete_tags_level_2, name='autocomplete_tags_level_2'),
    path('autocomplete_tags_level_3/', views.autocomplete_tags_level_3, name='autocomplete_tags_level_3'),


    path('ckeditor/', include('ckeditor_uploader.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
