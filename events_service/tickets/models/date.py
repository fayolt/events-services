from django.db import models

from . import Event, Venue

class Date(models.Model):
    """
    docstring
    """
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE)
    date = models.DateTimeField()

    def __str__(self):
        return f"{self.date}"