from  .views import *
from django.urls import path, include

urlpatterns = [
    path('', index,name="index"),
    path('travels/', travels),
    path('about/', about),
    #path('travels/<int:trid>/', travels),

]

handler404 = pageNotFound