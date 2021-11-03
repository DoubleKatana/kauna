from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    #path('home/', views.home, name='home'),
    path('gallery', views.gallery, name='gallery'),
    path('groom-bride', views.groom_bride, name='groom+bride'),
    path('guest', views.guest, name='guest'),
    path('when-where', views.when_where, name='when-where'),
]
