from tkinter import Menu
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from .models import *

menu = ["О сайте", "Создать пост", "Все статьи", "Войти"]

def index(request):
    return render(request, 'travels/index.html', {'menu':menu, 'title':'Главная страница'})

def about(request):
    return render(request, 'travels/about.html', {'menu':menu, 'title':'О сайте'})

def travels(request):
    travels = Travel.objects.all()
    return render(request, 'travels/travels.html', {'travels':travels, 'menu':menu, 'title':'Все статьи'})

def pageNotFound(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")