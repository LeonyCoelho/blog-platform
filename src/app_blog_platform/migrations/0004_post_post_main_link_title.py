# Generated by Django 5.0.2 on 2024-02-15 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_blog_platform', '0003_post_slide_images_post_post_main_link_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='post_main_link_title',
            field=models.CharField(max_length=500, null=True),
        ),
    ]