# Generated by Django 5.1.6 on 2025-03-26 03:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_remove_post_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.SlugField(default='default-slug'),
            preserve_default=False,
        ),
    ]
