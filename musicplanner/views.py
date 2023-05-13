from django.shortcuts import render, HttpResponse, redirect
from .models import MusicEntry, MusicForm, MarkDownloaded
from django.contrib.auth import authenticate, login


def index(request):
    if not request.user.is_authenticated:
        return redirect("/admin/")
    else:
        entries = MusicEntry.objects.filter(
                  ADDED_TO_LIBRARY=False).order_by('MADE')
        form = MusicForm()
        return render(request, 'musicplanner/base_main.html',
                      {'entries': entries, 'form': form})


def add_music(request):
    if not request.user.is_authenticated:
        return redirect("/admin/")

    if request.method == 'POST':
        form = MusicForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('mpindex')
    else:
        return redirect('mpindex')


def mark_as_added(request, id):
    if not request.user.is_authenticated:
        return redirect("/admin/")

    if request.method == 'POST':
        # TODO: any extra validation to see the POST is actually giving an id?
        entry = MusicEntry.objects.get(id=id)
        entry.ADDED_TO_LIBRARY = True
        entry.save()
        return redirect('mpindex')


def mark_as_downloaded(request, id):
    if not request.user.is_authenticated:
        return redirect("/admin/")

    if request.method == 'POST':
        entry = MusicEntry.objects.get(id=id)
        entry.DOWNLOADED = True
        entry.save()
        return redirect('mpindex')
