from django.contrib import admin

from .models import *


class TravelAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "time_create", "photo", "is_published", )
    list_editable = ("is_published",)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "title")
    

admin.site.register(Travel, TravelAdmin)
admin.site.register(Category, CategoryAdmin)

