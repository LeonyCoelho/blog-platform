from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields  import  RichTextUploadingField
from django.contrib.auth.models import User

class Theme(models.Model):
    theme_name= models.CharField(max_length=50)
    theme_url= models.CharField(max_length=50, default="default.css")
    def __str__(self):
        return self.theme_name

class Global_Settings(models.Model):
    blog_name = models.CharField(max_length=50, default='My Blog')
    theme = models.ManyToManyField(Theme)
    logo_image =  models.ImageField(upload_to='images/sys/logos/uploaded_logo/', default='images/sys/logos/logo.png')
    bg_image =  models.ImageField(upload_to='images/sys/bgs/uploaded_bgs/', default='images/sys/bgs/bg.png')
    bg_color = models.CharField(max_length=50, default=' ')
    show_author = models.BooleanField(default=False)

class About(models.Model):
    about_text = models.CharField(max_length=400, null=True)
    about_image = models.ImageField(upload_to='images/sys/about/')
    use_image = models.BooleanField(default=True)

class Home_Slide_Images(models.Model):
    home_slide_image = models.ImageField(upload_to='images/sys/home/')

class Home(models.Model):
    home_slide = models.ManyToManyField(Home_Slide_Images)
    use_slide = models.BooleanField(default=False)

class Tags_Level_1(models.Model):
    tag_name = models.CharField(max_length=60)

class Tags_Level_2(models.Model):
    parent_tag = models.ManyToManyField(Tags_Level_1)
    tag_name = models.CharField(max_length=60)

class Tags_Level_3(models.Model):
    parent_tag = models.ManyToManyField(Tags_Level_2)
    tag_name = models.CharField(max_length=60)

class Post_Slide_Images(models.Model):
    post_slide_image = models.ImageField(upload_to='images/post/')

    def __str__(self):
        return self.image.name

class Post(models.Model):
    post_name = models.CharField(max_length=120, null=False, default='Post Name')
    post_body = RichTextUploadingField(blank=True, null=True)
    post_date = models.DateField(auto_now_add=True)
    post_tag_level_1  = models.ManyToManyField(Tags_Level_1)
    post_tag_level_2  = models.ManyToManyField(Tags_Level_2)
    post_tag_level_3  = models.ManyToManyField(Tags_Level_3)
    post_main_link = models.CharField(max_length=500, null=True)
    post_main_link_title = models.CharField(max_length=500, null=True)
    post_cover_image = models.ImageField(upload_to='images/post/cover/', null=True)
    post_slide_images = models.ManyToManyField(Post_Slide_Images)