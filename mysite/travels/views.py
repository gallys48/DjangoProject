from tkinter import Menu
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from .models import *

menu = [{"title":"О сайте", 'url_name':'about'}, 
        {"title":"Создать пост", 'url_name':'add_travel'}, 
        {"title":"Все посты", 'url_name':'travels'}, 
        {"title":"Войти", 'url_name':'about'}]

def index(request):
    context = {
        'menu':menu,
        'title':'Главная страница'
    }
    return render(request, 'travels/index.html', context=context)

def about(request):
    context = {
        'menu':menu,
        'title':'О сайте'
    }
    return render(request, 'travels/about.html', context=context)

def travels(request):
    travels = Travel.objects.all()
    context = {
        'travels':travels,
        'menu':menu,
        'title':'Все статьи'
    }
    return render(request, 'travels/travels.html', context=context)

def addtravel(request):
    context = {
        'menu':menu,
        'title':'Создать пост'
    }
    return render(request, 'travels/addpost.html', context=context)



def pageNotFound(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")

def show_travel(request, travel_id):
    return HttpResponse(f"<h1>Отображение поста с id: {travel_id}</h1>")