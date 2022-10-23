from atexit import register
from  .views import *
from django.urls import path, include

urlpatterns = [
    path('', index, name="index"),
    path('travels/', TravelsList.as_view(), name="travels"),
    path('about/', about, name="about"),
    # path('register/', RegisterUser.as_view(), name="register"),
    # path('login/', register, name="login"),
    path('addtravel/', addtravel, name="add_travel"),
    path('travels/<slug:travel_slug>', ShowTravel.as_view(), name="travel"),
    path('category/<slug:cat_slug>', TravelsCategory.as_view(), name='category' )

]

handler404 = pageNotFound