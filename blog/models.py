from django.db import models


class BlogPost(models.Model):

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
    PUBLISHED = models.DateTimeField()
    PAML_CONTENT = models.TextField(blank=True)
    VISIBILITY = models.CharField(max_length=20,
                                  choices=VISIBILITY_CHOICES,
                                  default=PRIVATE)
    PINNED = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.TITLE} ({self.SHORT_TITLE})"
