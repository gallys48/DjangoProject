from email.policy import default
from enum import unique
from pyexpat import model
from tabnanny import verbose
from turtle import title
from unittest.util import _MAX_LENGTH
from django.db import models
from django.urls import reverse

class Travel(models.Model):
    title=models.CharField(max_length=255, verbose_name="Заголовок поста")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    content = models.TextField(blank=True, verbose_name="Текст поста")
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name="Фото")
    start_of_the_trip = models.DateField( verbose_name="Дата начала путешествия")
    end_of_the_trip = models.DateField( verbose_name="Дата окончания путешествия")
    expense = models.CharField(max_length=255, verbose_name="Затраченные средства")
    place = models.CharField(max_length=255, verbose_name="Место петешествия")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Время создания поста")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Время редактирования поста")
    is_published = models.BooleanField(default=True, verbose_name="Опубликован?")
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, blank=True, verbose_name="Категория поста")

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("travel", kwargs={"travel_slug": self.slug})

    class Meta:
        verbose_name = 'Пост о путешествии'
        verbose_name_plural = 'Посты о путешествии'
        ordering = ['time_create', 'title']

class Category(models.Model):
    title=models.CharField(max_length=100 , db_index=True, verbose_name="Название категории") 
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'