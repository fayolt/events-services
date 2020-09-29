from django.db import models

from . import Event, Timestamp

class Venue(Timestamp):
    """
    docstring
    """
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=255)
    capacity = models.PositiveIntegerField()
    events = models.ManyToManyField(Event, related_name="venues", through='Date')