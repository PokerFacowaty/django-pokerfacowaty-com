from django.shortcuts import render, redirect
from .models import Playlist
from django.conf import settings
from pathlib import Path
import csv


def index(request):
    playlists = Playlist.objects.filter(VISIBILITY='PU').order_by('TITLE')
    # all_csvs = []
    # for pl in playlists:
    #     with open(Path(settings.PLAYLIST_CSV_DIR) / pl.CSV_FILENAME,
    #               encoding="utf-8") as f:
    #         rdr = csv.DictReader(f, delimiter=";")
    #         parsed_csv = list(rdr)
    #     all_csvs.append(parsed_csv)

    # return render(request, 'playlists/base_main.html',
    #               {'all_csvs': all_csvs})
    return render(request, 'playlists/base_main.html',
                  {'playlists': playlists})


def playlist(request, short):
    if (Playlist.objects.get(SHORT_TITLE=short).VISIBILITY == "PR"
       and not request.user.is_authenticated):
        return redirect("/admin/")

    playlist = Playlist.objects.get(SHORT_TITLE=short)
    with open(Path(settings.PLAYLIST_CSV_DIR) / playlist.CSV_FILENAME, 
              encoding="utf-8") as f:
        rdr = csv.DictReader(f, delimiter=";")
        parsed_csv = list(rdr)
    return render(request, 'playlists/base_playlist.html',
                  {"playlist": playlist, 'csv': parsed_csv})
