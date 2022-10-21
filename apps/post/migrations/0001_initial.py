# Generated by Django 4.1.2 on 2022-10-21 12:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('title', models.CharField(max_length=30, unique=True)),
                ('slug', models.SlugField(blank=True, max_length=35, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('title', models.CharField(max_length=150)),
                ('slug', models.SlugField(blank=True, max_length=170, primary_key=True, serialize=False)),
                ('text', models.TextField()),
                ('image', models.ImageField(upload_to='post_images')),
                ('status', models.CharField(choices=[('open', 'Open'), ('closed', 'Closed'), ('draft', 'Draft')], default='draft', max_length=12)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('tag', models.ManyToManyField(blank=True, related_name='publications', to='post.tag')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='publications', to=settings.AUTH_USER_MODEL, verbose_name='Автор поста')),
            ],
            options={
                'ordering': ('created_at',),
            },
        ),
    ]
