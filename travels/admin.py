from django.contrib import admin

from .models import *


class TravelAdmin(admin.ModelAdmin):
    list_display = ("id", "author","title", "time_create", "photo", "is_published", )
    list_editable = ("is_published",)
    prepopulated_fields = {"slug" :("title",)}

class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "title")
    prepopulated_fields = {"slug" :("title",)}

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'birth_date', 'slug')
    list_display_links = ('user', 'slug')

class CountryAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    list_display_links = ('title', 'slug')

class CommentAdmin(admin.ModelAdmin):
    list_display = ("travel", "username","text", "created_date")
    

admin.site.register(Travel, TravelAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Profile, ProfileAdmin)
admin.site.register(Country, CountryAdmin)
admin.site.register(Comment, CommentAdmin)

