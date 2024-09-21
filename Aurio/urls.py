from django.urls import path
from . import views


urlpatterns = [
    path('songs/', views.songs, name='songs'),
     path('songs/<int:id>', views.songpost, name='songpost'),   
     
     path('tsongs/', views.songs, name='songs'),
     path('tsongs/<int:id>', views.tsongpost, name='tsongpost'),
     
     path('oldsongs/', views.songs, name='songs'),
     path('oldsongs/<int:id>', views.oldsongpost, name='oldsongpost'),
     
     path('usongs/', views.songs, name='usongs'),
     path('usongs/<int:id>', views.usongpost, name='usongpost'),
     
     path('watchlater', views.watchlater, name='watchlater'),
     path('login', views.login, name='login'),
     path('signup', views.signup, name='signup'),
     path('search', views.search, name='search'),
     path('c/<str:channel>', views.channel, name='channel'),
     path('upload', views.upload, name='upload'),
     ] 