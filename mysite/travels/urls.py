from atexit import register
from  .views import *
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', IndexPage.as_view(), name="index"),
    path('travels/', TravelsList.as_view(), name="travels"),
    path('usertravels/', UserTravelsList.as_view(), name="usertravels"),
    path('about/', AboutPage.as_view(), name="about"),
    path('register/', RegisterUser.as_view(), name="register"),
    path('login/', LoginUser.as_view(), name="login"),
    path('logut', logout_user, name="logout"),
    path('addtravel/', addtravel, name="add_travel"),
    path('travels/<slug:travel_slug>', ShowTravel.as_view(), name="travel"),
    path('category/<slug:cat_slug>', TravelsCategory.as_view(), name='category' )

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = pageNotFound