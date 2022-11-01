from django.contrib.auth.views import LoginView
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import *
from django.contrib.auth.forms import *
from django.contrib.auth import logout, login
from django.contrib.auth.decorators import login_required
from django.urls import *
from .utils import DataMixin

from  .forms import *
from .models import *

menu = [{"title":"О сайте", 'url_name':'about'}, 
        {"title":"Создать пост", 'url_name':'add_travel'}, 
        {"title":"Все посты", 'url_name':'travels'},]

class IndexPage(DataMixin, TemplateView):
    template_name= 'travels/index.html'
    
    def get_context_data(self, *,object_list=None,**kwargs):
         context = super().get_context_data(**kwargs)
         c_def = self.get_user_context(title="Главная страница")
         return dict(list(context.items())+(list(c_def.items())))
     
# def index(request):
#     context = {
#         'menu':menu,
#         'title':'Главная страница'
#     }
#     return render(request, 'travels/index.html', context=context)

# def about(request):
#     context = {
#         'menu':menu,
#         'title':'О сайте'
#     }
#     return render(request, 'travels/about.html', context=context)

class AboutPage(DataMixin, TemplateView):
    template_name= 'travels/about.html'
    
    def get_context_data(self, *,object_list=None,**kwargs):
         context = super().get_context_data(**kwargs)
         c_def = self.get_user_context(title="О сайте")
         return dict(list(context.items())+(list(c_def.items())))

class TravelsList(DataMixin, ListView):
    paginate_by = 6
    model= Travel
    template_name= 'travels/travels.html'
    context_object_name= 'travels'

    def get_context_data(self, *,object_list=None,**kwargs):
         context = super().get_context_data(**kwargs)
         c_def = self.get_user_context(title="Все посты")
         return dict(list(context.items())+(list(c_def.items())))

    def get_queryset(self):
        return Travel.objects.filter(is_published=True)
    

@login_required
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
                Travel.objects.create(author=request.user,**form.cleaned_data)
                return redirect('travels')
            except:
                form.add_error(None, "Ошибка добавления поста")

    else:
        print("Ошибка")
        form=AddTravelForm()

    return render(request, 'travels/add_post.html', context=context)



def pageNotFound(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")


class ShowTravel(DataMixin, DetailView):
    model = Travel
    template_name = 'travels/travel.html'
    slug_url_kwarg = 'travel_slug'
    context_object_name = 'travel'
    def get_context_data(self, *,object_list=None,**kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=context['travel'])
        return dict(list(context.items())+(list(c_def.items())))

class UpdateTravel(DataMixin, UpdateView):
    model = Travel
    template_name = 'travels/update_post.html'
    slug_url_kwarg = 'travel_slug'
    success_url = reverse_lazy('usertravels')
    fields = ['title', 'content', 'photo', 'start_of_the_trip', 'end_of_the_trip', 'expense', 'place', 'cat']
    def get_context_data(self, *,object_list=None,**kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=context['travel'])
        return dict(list(context.items())+(list(c_def.items())))

class DeleteTravel(DataMixin, DeleteView):
    model = Travel
    template_name = 'travels/delete_post.html'
    slug_url_kwarg = 'travel_slug'
    success_url = reverse_lazy('usertravels')
    fields = ['title', 'slug', 'content', 'photo', 'start_of_the_trip', 'end_of_the_trip', 'expense', 'place', 'cat']
    def get_context_data(self, *,object_list=None,**kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=context['travel'])
        return dict(list(context.items())+(list(c_def.items())))
        



class TravelsCategory(DataMixin, ListView):
    paginate_by = 6
    model= Travel
    template_name= 'travels/travels.html'
    context_object_name= 'travels'
    allow_empty = False

    def get_context_data(self, *,object_list=None,**kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Категория - '+str(context['travels'][0].cat),
                                      cat_selected=context['travels'][0].cat_id)
        return dict(list(context.items())+(list(c_def.items())))
        
    
    def get_queryset(self):
        return Travel.objects.filter(cat__slug=self.kwargs['cat_slug'], is_published=True)

class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'travels/register.html'
    success_url = reverse_lazy('login')
    
    def get_context_data(self, *,object_list=None,**kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Регистрация')
        return dict(list(context.items())+(list(c_def.items())))
    
    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('travels')

class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'travels/login.html'
    success_url = reverse_lazy('usertravels')
    def get_context_data(self, *,object_list=None,**kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Авторизация')
        return dict(list(context.items())+(list(c_def.items())))

def logout_user(request):
    logout(request)
    return redirect('login')

class UserTravelsList(DataMixin, ListView):
    paginate_by = 3
    model= Travel
    template_name= 'travels/user_travels.html'
    context_object_name= 'travels'
    allow_empty = False

    def get_context_data(self, *,object_list=None,**kwargs):
         context = super().get_context_data(**kwargs)
         c_def = self.get_user_context(title='Посты пользователя '+str(context['travels'][0].author))
         return dict(list(context.items())+(list(c_def.items())))

    def get_queryset(self):
        return Travel.objects.filter(author=self.request.user)