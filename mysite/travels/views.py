from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render

def index(request):
    return HttpResponse("Страница приложения travels")

def travels(request, tr):
    return HttpResponse(f"<h1>Все статьи</h1><p>{tr}</p>")

def pageNotFound(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")