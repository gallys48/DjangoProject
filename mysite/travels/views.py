import imp
from multiprocessing import context
from tkinter import Menu
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView

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

# def travels(request):
#     travels = Travel.objects.all()
#     context = {
#         'travels':travels,
#         'menu':menu,
#         'title':'Все статьи'
#     }
#     return render(request, 'travels/travels.html', context=context)

class TravelsList(ListView):
    model= Travel
    template_name= 'travels/travels.html'
    context_object_name= 'travels'

    def get_context_data(self, *,object_list=None,**kwargs):
         context = super().get_context_data(**kwargs)
         context['menu']=menu
         context['title'] = 'Все посты'
         context['cat_selected'] = 0
         return context
    
    def get_queryset(self):
        return Travel.objects.filter(is_published=True)
    


def addtravel(request):
    form = AddTravelForm()
    context = {
        'menu':menu,
        'title':'Создать пост',
        'form': form
    }

    if request.method=='POST':
        form=AddTravelForm(request.POST, request.FILES)
        if form.is_valid():
            #print(form.cleaned_data)
            try:
                Travel.objects.create(**form.cleaned_data)
                return redirect('travels')
            except:
                form.add_error(None, "Ошибка добавления поста")

    else:
        print("Ошибка")
        form=AddTravelForm()

    return render(request, 'travels/addpost.html', context=context)



def pageNotFound(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")

# def show_travel(request, travel_slug):
#     travel = get_object_or_404(Travel, slug=travel_slug)

#     context={
#         'travel' : travel,
#         'menu' : menu,
#         'title': travel.title
#     }

#     return render(request, 'travels/travel.html', context=context)
class ShowTravel(DetailView):
    model = Travel
    template_name = 'travels/travel.html'
    slug_url_kwarg = 'travel_slug'
    context_object_name = 'travel'
    def get_context_data(self, *,object_list=None,**kwargs):
         context = super().get_context_data(**kwargs)
         context['menu']=menu
         context['title'] = context['travel']
         return context

class TravelsCategory(ListView):
    model= Travel
    template_name= 'travels/travels.html'
    context_object_name= 'travels'
    allow_empty = False

    def get_context_data(self, *,object_list=None,**kwargs):
         context = super().get_context_data(**kwargs)
         context['menu']=menu
         context['title'] = 'Категория -' + str(context['travels'][0].cat)
         context['cat_selected'] = context['travels'][0].cat_id
         return context
    
    def get_queryset(self):
        return Travel.objects.filter(cat__slug=self.kwargs['cat_slug'], is_published=True)