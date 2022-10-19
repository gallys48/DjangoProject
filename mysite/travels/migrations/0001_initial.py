# Generated by Django 3.0.14 on 2022-10-19 14:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=100, verbose_name='Название категории')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='URL')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Travel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Заголовок поста')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='URL')),
                ('content', models.TextField(blank=True, verbose_name='Тесет поста')),
                ('photo', models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фото')),
                ('start_of_the_trip', models.DateTimeField(verbose_name='Время начала путешествия')),
                ('end_of_the_trip', models.DateTimeField(verbose_name='Время окончания путешествия')),
                ('expense', models.CharField(max_length=255, verbose_name='Затраченные средства')),
                ('place', models.CharField(max_length=255, verbose_name='Место петешествия')),
                ('time_create', models.DateTimeField(auto_now_add=True, verbose_name='Время создания поста')),
                ('time_update', models.DateTimeField(auto_now=True, verbose_name='Время редактирования поста')),
                ('is_published', models.BooleanField(default=True, verbose_name='Опубликован?')),
                ('cat', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, to='travels.Category', verbose_name='Категория поста')),
            ],
            options={
                'verbose_name': 'Пост о путешествии',
                'verbose_name_plural': 'Посты о путешествии',
                'ordering': ['time_create', 'title'],
            },
        ),
    ]
