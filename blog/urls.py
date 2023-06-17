from django.urls import path
from . import views

urlpatterns = [
    path('<str:short>', views.post, name='post'),
    path('', views.index, name='blog')
]
