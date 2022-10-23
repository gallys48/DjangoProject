
from multiprocessing import context
from typing import Counter

from .models import *

from django.db.models.aggregates import *


menu = [{"title":"О сайте", 'url_name':'about'}, 
        {"title":"Создать пост", 'url_name':'add_travel'}, 
        {"title":"Все посты", 'url_name':'travels'},]

class DataMixin:
    def get_user_context(self, **kwargs):
        paginate_by = 3
        context=kwargs
        cats = Category.objects.all()
        context['menu'] = menu
        context['cats'] = cats
        if 'cat_selected' not in context:
            context['cat_selected'] = 0
        return context