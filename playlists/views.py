from django.shortcuts import render, redirect
from .models import Playlist
from django.conf import settings
from pathlib import Path
import csv


def index(request):
    playlists = Playlist.objects.filter(VISIBILITY='PU').order_by('TITLE')
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
        parsed_csv = []
        for nr, line in enumerate(rdr):
            parsed_csv.append(line)
            if isinstance(parsed_csv[-1]["Duration"], str):
                dur_secs = parsed_csv[-1]["Duration"].split(".")[0]
                # TODO: replace it with datetime probably
                if int(dur_secs) % 60 >= 10:
                    parsed_csv[-1]["Duration"] = (f"{int(dur_secs) // 60}"
                                                + f":{int(dur_secs) % 60}")
                else:
                    parsed_csv[-1]["Duration"] = (f"{int(dur_secs) // 60}"
                                                + f":0{int(dur_secs) % 60}")
            else:
                parsed_csv[-1]["Duration"] = "N/A"
            parsed_csv[-1]["Nr"] = nr + 1
        sorted_by = request.GET.get('sortby', 'Nr')
        rev = request.GET.get('reverse', 'False') == 'True'
        parsed_csv.sort(key=lambda x: x[sorted_by], reverse=rev)
    return render(request, 'playlists/base_playlist.html',
                  {"playlist": playlist, 'csv': parsed_csv})
