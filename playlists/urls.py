from django.urls import path
from . import views

urlpatterns = [
    path('<str:short>', views.playlist, name='playlist'),
    path('', views.index, name='playlists')
]
