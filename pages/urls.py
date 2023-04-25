from django.urls import path
from . import views

urlpatterns = [
    path('archive/', views.archive, name='archive'),
    path('dating/', views.dating, name='dating'),
    path('<str:short>/', views.pamlpage, name='paml'),
    path('', views.index, name='main')
]
