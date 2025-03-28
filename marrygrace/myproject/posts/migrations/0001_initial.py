# filepath: /c:/Users/marrygrace/myproject/posts/migrations/0001_initial.py
# Generated by Django 5.1.6 on 2025-03-24 02:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('body', models.TextField()),  # Updated field name
                ('slug', models.SlugField()),  # Added slug field
                ('date', models.DateTimeField(auto_now_add=True)),  # Added date field
            ],
        ),
    ]