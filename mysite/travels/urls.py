from  .views import *
from django.urls import path, include

urlpatterns = [
    path('', index, name="index"),
    path('travels/', travels, name="travels"),
    path('about/', about, name="about"),
    path('addtravel/', addtravel, name="add_travel"),
    # path('travels/<int:travel_id>', show_travel, name="show_travel"),
    #path('travels/<int:trid>/', travels),

]

handler404 = pageNotFound