from django.contrib.auth.views import LoginView
from django.http import HttpResponseNotFound, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import *
from django.contrib.auth.forms import *
from django.contrib.auth import logout, login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect

from django.urls import *
from .utils import DataMixin
from django.db import transaction
import json

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


class ShowTravel(View):

    def get(self, request, slug, *args, **kwargs):
        travel = get_object_or_404(Travel, slug=slug)
        comment_form = CommentForm()
        return render(request, 'travels/travel.html', context={
            'travel': travel,
            'menu':menu,
            'comment_form': comment_form
    })
    
    
    def post(self, request, slug, *args, **kwargs):
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            text = request.POST['text']
            username = self.request.user
            travel = get_object_or_404(Travel, slug = slug)
            comment = Comment.objects.create(travel=travel, username=username, text=text)
            return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
        return render(request, 'travels/travel.html', context={
            'comment_form': comment_form
        })


class UpdateTravel(DataMixin, UpdateView):
    form_class = EditTravelForm
    model = Travel
    template_name = 'travels/update_post.html'
    slug_url_kwarg = 'travel_slug'
    success_url = reverse_lazy('my_usertravels')
    def get_context_data(self, *,object_list=None,**kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=context['travel'])
        return dict(list(context.items())+(list(c_def.items())))
    
    def get_success_url(self):
        return reverse_lazy('my_usertravels', kwargs={'my_slug': self.object.author.profile.slug})

class DeleteTravel(DataMixin, DeleteView):
    model = Travel
    template_name = 'travels/delete_post.html'
    slug_url_kwarg = 'travel_slug'
    success_url = reverse_lazy('my_usertravels')
    
    def get_context_data(self, *,object_list=None,**kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=context['travel'])
        return dict(list(context.items())+(list(c_def.items())))
    
    def get_success_url(self):
        return reverse_lazy('my_usertravels', kwargs={'my_slug': self.object.author.profile.slug})
        



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
        return redirect('my_profile_detail')

class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'travels/login.html'
    success_url = reverse_lazy('my_profile_detail')
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
    allow_empty = True
    slug_url_kwarg = 'profile_user'

    
    def get_context_data(self, *,object_list=None,**kwargs):
         context = super().get_context_data(**kwargs)
         c_def = self.get_user_context(title='Посты пользователя '+str(context['travels'][0].author), author = context['travels'][0].author)
         return dict(list(context.items())+(list(c_def.items())))
    
    def get_queryset(self):
        return Travel.objects.filter(author=self.kwargs['profile_user'], is_published=True)

class MyTravelsList(DataMixin, ListView):
    paginate_by = 3
    model= Travel
    template_name= 'travels/my_travels.html'
    context_object_name= 'travels'
    allow_empty = True
    slug_url_kwarg = 'my_slag'

    
    def get_context_data(self, *,object_list=None,**kwargs):
         context = super().get_context_data(**kwargs)
         c_def = self.get_user_context(title='Посты пользователя '+str(context['travels'][0].author), author = context['travels'][0].author)
         return dict(list(context.items())+(list(c_def.items())))
    
    def get_queryset(self):
        return Travel.objects.filter(author=self.request.user)
    
class ProfileDetailView(DataMixin, DetailView):

    model = Profile
    context_object_name = 'profile'
    template_name = 'travels/profile_detail.html'
    slug_url_kwarg = 'profile_slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=f'Страница пользователя: {self.object.user.username}')
        return dict(list(context.items())+(list(c_def.items())))

class MyProfileDetailView(DataMixin, DetailView):

    model = Profile
    context_object_name = 'profile'
    template_name = 'travels/my_profile_detail.html'
    slug_url_kwarg = 'profile_slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=f'Страница пользователя: {self.object.user.username}')
        return dict(list(context.items())+(list(c_def.items())))

class ProfileUpdateView(DataMixin, UpdateView):

    model = Profile
    form_class = ProfileUpdateForm
    template_name = 'travels/update_profile.html'
    slug_url_kwarg = 'profile_slug'
    success_url = reverse_lazy('my_profile_detail')
    

    def get_object(self, queryset=None):
        return self.request.user.profile

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=f'Редактирование профиля пользователя: {self.request.user.username}')
        if self.request.POST:
            context['user_form'] = UserUpdateForm(self.request.POST, instance=self.request.user)
        else:
            context['user_form'] = UserUpdateForm(instance=self.request.user)
        return dict(list(context.items())+(list(c_def.items())))

    def form_valid(self, form):
        context = self.get_context_data()
        user_form = context['user_form']
        with transaction.atomic():
            if all([form.is_valid(), user_form.is_valid()]):
                user_form.save()
                form.save()
            else:
                context.update({'user_form': user_form})
                return self.render_to_response(context)
        return super(ProfileUpdateView, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('profile_detail', kwargs={'slug': self.object.slug})
