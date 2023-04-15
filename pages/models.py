from django.db import models


class PaMLPage(models.Model):

    PUBLIC = 'PU'
    PRIVATE = 'PR'
    VISIBILITY_CHOICES = [(PUBLIC, 'Public'),
                          (PRIVATE, 'Private')]
    TITLE = models.CharField(max_length=100)
    SHORT_TITLE = models.CharField(max_length=20)
    LAST_EDITED = models.DateTimeField()
    PAML_CONTENT = models.TextField(blank=True)
    VISIBILITY = models.CharField(max_length=20,
                                  choices=VISIBILITY_CHOICES,
                                  default=PRIVATE)

    def __str__(self):
        return f"{self.TITLE} ({self.SHORT_TITLE})"
