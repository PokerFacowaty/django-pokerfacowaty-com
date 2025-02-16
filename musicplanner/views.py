from django.shortcuts import render, HttpResponse, redirect
from .models import MusicEntry, MusicForm, MarkDownloaded
from django.contrib.auth import authenticate, login
from musicplanner.serializers import MusicSerializer
from rest_framework import generics, permissions
from django.contrib.auth.decorators import login_required


@login_required
def index(request):
    entries = MusicEntry.objects.filter(
              ADDED_TO_LIBRARY=False).order_by('MADE')
    form = MusicForm()
    return render(request, 'musicplanner/base_main.html',
                  {'entries': entries, 'form': form})


@login_required
def add_music(request):
    if request.method == 'POST':
        form = MusicForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('mpindex')
    else:
        return redirect('mpindex')


@login_required
def mark_as_added(request, id):
    if request.method == 'POST':
        # TODO: any extra validation to see the POST is actually giving an id?
        entry = MusicEntry.objects.get(id=id)
        entry.ADDED_TO_LIBRARY = True
        entry.save()
        return redirect('mpindex')


@login_required
def mark_as_downloaded(request, id):
    if request.method == 'POST':
        entry = MusicEntry.objects.get(id=id)
        entry.DOWNLOADED = True
        entry.save()
        return redirect('mpindex')


class MusicList(generics.ListCreateAPIView):
    queryset = MusicEntry.objects.all()
    serializer_class = MusicSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class MusicEntryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = MusicEntry.objects.all()
    serializer_class = MusicSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
