# Generated by Django 5.0.2 on 2024-02-23 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_blog_platform', '0005_post_post_tag_level_1'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='post_cover_image',
            field=models.ImageField(null=True, upload_to='images/cover/'),
        ),
    ]
