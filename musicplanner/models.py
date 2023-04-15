from django.db import models
from django.forms import ModelForm, Textarea, TextInput


class MusicEntry(models.Model):
    MADE = models.DateField(auto_now_add=True)
    ARTIST = models.CharField(max_length=50, blank=True)
    ALBUM = models.CharField(max_length=50, blank=True)
    SONGS = models.CharField(max_length=250, blank=True)
    NOTE = models.TextField(blank=True)
    DOWNLOADED = models.BooleanField(default=False)
    ADDED_TO_LIBRARY = models.BooleanField(default=False)

    def __str__(self):
        if self.ARTIST and self.ALBUM and not self.SONGS:
            # entire album with artist specified
            return f"{self.ARTIST} - {self.ALBUM}"
        elif not self.ARTIST and self.ALBUM and not self.SONGS:
            # entire album without an artist (compilation)
            return f"{self.ALBUM}"
        elif self.ARTIST and self.SONGS:
            # song(s) wtih artist specified
            # IMPORTANT: songs are in a str, not a list
            return f"{self.ARTIST}: {self.SONGS}"
        else:
            # Very important to never let it return None
            return f"{self.id}"


class MusicForm(ModelForm):
    class Meta:
        model = MusicEntry
        fields = ['ARTIST', 'SONGS', 'ALBUM', 'NOTE']
        widgets = {
            'ARTIST': TextInput(attrs={'class': 'input'}),
            'SONGS': TextInput(attrs={'class': 'input'}),
            'ALBUM': TextInput(attrs={'class': 'input'}),
            'NOTE': TextInput(attrs={'class': 'input'}),
        }


class MarkDownloaded(ModelForm):
    class Meta:
        model = MusicEntry
        fields = ['DOWNLOADED']
