# Generated by Django 5.0.2 on 2024-02-28 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_blog_platform', '0008_about_use_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='home',
            name='use_slide',
            field=models.BooleanField(default=False),
        ),
    ]