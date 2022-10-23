from atexit import register
from django import template
from travels.models import *

register = template.Library()

@register.simple_tag()
def get_categories():
    return Category.objects.all()