from django.db import models

from . import Event, Timestamp


class Venue(Timestamp):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=255)
    capacity = models.PositiveIntegerField()
    events = models.ManyToManyField(
        Event, related_name="venues", through='Date')

    def __str__(self):
        return f"{self.name} @ {self.address}, {self.capacity} places"
