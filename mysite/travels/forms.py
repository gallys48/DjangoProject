from dataclasses import field
import re
from xml.dom import ValidationErr
from django import forms
from django.contrib.admin.widgets import *
from django.core.exceptions import ValidationError

from .models import *



class AddTravelForm(forms.Form):
    title = forms.CharField(max_length=255, label='Заголовок')
    slug = forms.SlugField(max_length=255, label='URL')
    content = forms.CharField(widget=forms.Textarea(attrs={'cols':60, 'rows': 10}), label='Текст поста')
    photo = forms.ImageField(label='Фото поста')
    start_of_the_trip = forms.DateTimeField(label='Время начала путешествия', widget=AdminSplitDateTime)
    end_of_the_trip = forms.DateTimeField(label='Время окончания путешествия', widget=AdminSplitDateTime)
    expense = forms.CharField(max_length=255, label='Затраты на путешествие')
    place = forms.CharField(max_length=255, label='Место путешествия')
    is_published = forms.BooleanField(label='Опубликован', required=False, initial=True)
    cat = forms.ModelChoiceField(queryset=Category.objects.all(),label='Категория', empty_label="Категория не выбрана")
    # class Meta:
    #     model = Travel
    #     fields = '__all__'
    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) > 200:
            raise ValidationError('Длина превышает 200 символов')
        return title