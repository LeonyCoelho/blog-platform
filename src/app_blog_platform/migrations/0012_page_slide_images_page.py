# Generated by Django 5.0.2 on 2024-03-08 18:49

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_blog_platform', '0011_alter_post_post_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Page_Slide_Images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('page_slide_image', models.ImageField(upload_to='images/page/')),
            ],
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('page_name', models.CharField(default='Page Name', max_length=120)),
                ('page_body', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
                ('page_date', models.DateField(blank=True, null=True)),
                ('page_main_link', models.CharField(max_length=500, null=True)),
                ('page_main_link_title', models.CharField(max_length=500, null=True)),
                ('page_cover_image', models.ImageField(null=True, upload_to='images/page/cover/')),
                ('page_tag_level_1', models.ManyToManyField(to='app_blog_platform.tags_level_1')),
                ('page_tag_level_2', models.ManyToManyField(to='app_blog_platform.tags_level_2')),
                ('page_tag_level_3', models.ManyToManyField(to='app_blog_platform.tags_level_3')),
                ('page_slide_images', models.ManyToManyField(to='app_blog_platform.page_slide_images')),
            ],
        ),
    ]
