from dataclasses import field
import re
from tkinter import Widget
from xml.dom import ValidationErr
from django import forms
from django.contrib.admin.widgets import *
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import *
from django.contrib.auth.models import *

from .models import *



class AddTravelForm(forms.Form):
    title = forms.CharField(max_length=255, label='Заголовок')
    slug = forms.SlugField(max_length=255, label='URL')
    content = forms.CharField(widget=forms.Textarea(attrs={'cols':60, 'rows': 10}), label='Текст поста')
    photo = forms.ImageField(label='Фото поста')
    start_of_the_trip = forms.DateField(label='Дата начала путешествия', widget=AdminDateWidget)
    end_of_the_trip = forms.DateField(label='Дата окончания путешествия', widget=AdminDateWidget)
    expense = forms.CharField(max_length=255, label='Затраты на путешествие')
    place = forms.CharField(max_length=255, label='Место путешествия')
    cat = forms.ModelChoiceField(queryset=Category.objects.all(),label='Категория', empty_label="Категория не выбрана")
    # class Meta:
    #     model = Travel
    #     fields = '__all__'
    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) > 200:
            raise ValidationError('Длина превышает 200 символов')
        return title

class RegisterUserForm(UserCreationForm):
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class':'form-input'}))
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={'class':'form-input'}))
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class':'form-input'}))
    
    email = forms.EmailField(label='Электронная почта', widget=forms.EmailInput(attrs={'class':'form-input'}))
    
    field_order = ['username', 'email', 'password1', 'password2']
    class Meta:
        model = User
        fields = {'username',  'email', 'password2', 'password1'}

class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class':'form-input'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class':'form-input'}))
    
