
from multiprocessing import context
from typing import Counter

from .models import *

from django.db.models.aggregates import *


menu = [{"title":"О сайте", 'url_name':'about'}, 
        {"title":"Создать пост", 'url_name':'add_travel'}, 
        {"title":"Все посты", 'url_name':'travels'},]

class DataMixin:
    def get_user_context(self, **kwargs):
        paginate_by = 6
        context=kwargs
        cats = Category.objects.all()
        
        user_menu=menu.copy()
        if not self.request.user.is_authenticated:
            user_menu.pop(1)
        
        context['menu'] = user_menu
        context['cats'] = cats
        if 'cat_selected' not in context:
            context['cat_selected'] = 0
        return context