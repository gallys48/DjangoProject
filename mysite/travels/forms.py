from django import forms
from django.contrib.admin.widgets import *

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
    is_published = forms.BooleanField(label='Опубликован', required=False, initial=True)
    cat = forms.ModelChoiceField(queryset=Category.objects.all(),label='Категория', empty_label="Категория не выбрана")