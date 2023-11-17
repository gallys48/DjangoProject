from atexit import register
from  .views import *
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', IndexPage.as_view(), name="index"),
    path('all-travels/', TravelsList.as_view(), name="travels"),
    path('<int:profile_user>/<str:profile_name>/travels', UserTravelsList.as_view(), name="usertravels"),
    path('<slug:my_slug>/travels', MyTravelsList.as_view(), name="my_usertravels"),
    path('about/', AboutPage.as_view(), name="about"),
    path('register/', RegisterUser.as_view(), name="register"),
    path('login/', LoginUser.as_view(), name="login"),
    path('logut', logout_user, name="logout"),
    path('addtravel/', addtravel, name="add_travel"),
    path('<slug:profile_slug>/edit', ProfileUpdateView.as_view(), name='profile_edit'),
    path('me-<slug:profile_slug>', MyProfileDetailView.as_view(), name='my_profile_detail'),
    path('<slug:profile_slug>', ProfileDetailView.as_view(), name='profile_detail'),
    re_path('travels/(?P<travel_slug>[-a-zA-Z0-9-а-яA]+)/delete/', DeleteTravel.as_view(), name='travel_delete'),
    re_path('travels/(?P<travel_slug>[-a-zA-Z0-9-а-яA]+)/edit/', UpdateTravel.as_view(), name='travel_update'),
    re_path('travels/(?P<travel_slug>[-a-zA-Z0-9-а-яA]+)', ShowTravel.as_view(), name="travel"),
    path('category/<slug:cat_slug>', TravelsCategory.as_view(), name='category' ),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = pageNotFound