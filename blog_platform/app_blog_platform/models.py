from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields  import RichTextUploadingField
from django.contrib.auth.models import User

class Theme(models.Model):
    theme_name= models.CharField(max_length=50)
    theme_url= models.CharField(max_length=50, default="default.css")
    def __str__(self):
        return self.theme_name

class Global_Settings(models.Model):
    blog_name = models.CharField(max_length=50, default='My Blog')
    theme = models.ManyToManyField(Theme)
    logo_image =  models.ImageField(upload_to='logos/uploaded_logo', default='logos/logo.png')
    bg_image =  models.ImageField(upload_to='bgs/uploaded_bgs', default='bgs/bg.png')
    bg_color = models.CharField(max_length=50, default=' ')
    show_author = models.BooleanField(default=False)

class Tags_Level_1(models.Model):
    tag_name = models.CharField(max_length=60)

class Tags_Level_2(models.Model):
    parent_tag = models.ManyToManyField(Tags_Level_1)
    tag_name = models.CharField(max_length=60)

class Tags_Level_3(models.Model):
    parent_tag = models.ManyToManyField(Tags_Level_2)
    tag_name = models.CharField(max_length=60)

class Post(models.Model):
    post_name = models.CharField(max_length=120, null=False, default='Post Name')
    post_body = RichTextUploadingField(blank=True, null=True)
    post_date = models.DateField(auto_now_add=True)
    post_tag_level_2  = models.ManyToManyField(Tags_Level_2)
    post_tag_level_3  = models.ManyToManyField(Tags_Level_3)