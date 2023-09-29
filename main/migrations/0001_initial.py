# Generated by Django 4.2.5 on 2023-09-29 13:05

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='email address')),
                ('username', models.CharField(blank=True, max_length=30, unique=True, verbose_name='name')),
                ('is_staff', models.BooleanField(default=False, verbose_name='staff')),
                ('is_superuser', models.BooleanField(default=False, verbose_name='superuser')),
                ('avatar', models.ImageField(blank=True, default='avatar.svg', upload_to='avatar/%Y-%m-%d/', verbose_name='avatar')),
                ('can_manage_article', models.BooleanField(default=True, verbose_name='can manage article')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, verbose_name='title')),
                ('content', ckeditor.fields.RichTextField(blank=True, verbose_name='content')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='date')),
                ('slug', models.SlugField(unique=True, verbose_name='slug')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='author')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, verbose_name='title')),
                ('slug', models.SlugField(unique=True, verbose_name='slug')),
            ],
        ),
        migrations.CreateModel(
            name='Ip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='text')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='date')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.article', verbose_name='article')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='author')),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='category',
            field=models.ManyToManyField(blank=True, to='main.category', verbose_name='category'),
        ),
        migrations.AddField(
            model_name='article',
            name='views',
            field=models.ManyToManyField(blank=True, related_name='post_views', to='main.ip'),
        ),
    ]
