from django.db import models


class Playlist(models.Model):

    PUBLIC = 'PU'
    UNLISTED = 'UN'
    PRIVATE = 'PR'
    VISIBILITY_CHOICES = [
                          (PUBLIC, 'Public'),
                          (UNLISTED, 'Unlisted'),
                          (PRIVATE, 'Private')
                         ]
    TITLE = models.CharField(max_length=100)
    SHORT_TITLE = models.CharField(max_length=20)
    LAST_UPDATED = models.DateTimeField()
    CSV_FILENAME = models.CharField(max_length=100)
    DESCRIPTION = models.TextField(blank=True)
    VISIBILITY = models.CharField(max_length=20,
                                  choices=VISIBILITY_CHOICES,
                                  default=PRIVATE)

    def __str__(self):
        return f"{self.TITLE} ({self.SHORT_TITLE})"
