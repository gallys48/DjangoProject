from  .views import *
from django.urls import path, include

urlpatterns = [
    path('', index,name="index"),
    path('travels/<slug:tr>/', travels),
    #path('travels/<int:trid>/', travels),

]

handler404 = pageNotFound