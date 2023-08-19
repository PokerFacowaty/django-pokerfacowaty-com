from django.urls import path
from . import views
from rest_framework.urlpatters import format_suffix_patterns

urlpatterns = [
    path('music-entries/', views.MusicList.as_view()),
    path('music-entries/<int:pk>/', views.MusicEntryDetail.as_view()),
    path('mark-downloaded/<int:id>', views.mark_as_downloaded,
         name='mark_downloaded'),
    path('mark-added/<int:id>', views.mark_as_added, name="mark_added"),
    path('add', views.add_music, name='add_music'),
    path('', views.index, name='mpindex'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
