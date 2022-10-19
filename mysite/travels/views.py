from tkinter import Menu
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, get_object_or_404
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

def show_travel(request, travel_id):
    # travel = get_object_or_404(Travel, pk=travel_id)
    # context = {
    #     'travel':travel,
    #     'menu':menu,
    #     'title':travel.title,
        
    # }
    return render(request, 'travels/travel.html', context=context)

def pageNotFound(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")
