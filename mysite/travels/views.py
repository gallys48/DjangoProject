from tkinter import Menu
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, get_object_or_404, redirect

from  .forms import *
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
    form = AddTravelForm()
    context = {
        'menu':menu,
        'title':'Создать пост',
        'form': form
    }

    if request.method=='POST':
        form=AddTravelForm(request.POST)
        if form.is_valid():
            #print(form.cleaned_data)
            try:
                Travel.objects.create(**form.cleaned_data)
                return redirect('home')
            except:
                form.add_error(None, 'Ошибка добавления поста')
    else:
        form=AddTravelForm()

    return render(request, 'travels/addpost.html', context=context)



def pageNotFound(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")

def show_travel(request, travel_slug):
    travel = get_object_or_404(Travel, slug=travel_slug)

    context={
        'travel' : travel,
        'menu' : menu,
        'title': travel.title
    }

    return render(request, 'travels/travel.html', context=context)