from rest_framework import serializers
from musicplanner.models import MusicEntry


class MusicSerializer(serializers.ModelSerializer):
    class Meta:
        model = MusicEntry
        fields = ["id", "ARTIST", "ALBUM", "SONGS", "NOTE", "DOWNLOADED",
                  "ADDED_TO_LIBRARY"]
