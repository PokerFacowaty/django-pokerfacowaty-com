from django.shortcuts import render
from .models import Playlist
from django.conf import settings
from pathlib import Path


def index(request):
    playlists = Playlist.objects.filter(VISIBILITY='PU').order_by('TITLE')
    csv_paths = []
    for playlist in playlists:
        csv_paths.append(str(Path(settings.PLAYLIST_CSV_DIR
                                  / playlist.CSV_FILENAME)))
    return render(request, 'playlists/base_main.html',
                  {'csv_paths': csv_paths})
