from django.shortcuts import render


def index(request):
    return render(request, 'playlists/base_main.html')
