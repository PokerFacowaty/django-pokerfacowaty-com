from django.urls import path
from . import views

urlpatterns = [
    path('mark-downloaded/<int:id>', views.mark_as_downloaded,
         name='mark_downloaded'),
    path('mark-added/<int:id>', views.mark_as_added, name="mark_added"),
    path('add', views.add_music, name='add_music'),
    path('', views.index, name='mpindex'),
]
