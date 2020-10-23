from django.contrib.postgres.fields import ArrayField
from django.db import models

from .timestamp import Timestamp

class Event(Timestamp):
    """
    docstring
    """
    title = models.CharField(max_length=255)
    type = models.CharField(max_length=20, blank=True)
    promoter = models.CharField(max_length=255, blank=True)
    tags = ArrayField(models.CharField(max_length=20, blank=True))

    def __str__(self):
        return f"{self.type}: {self.title} by {self.promoter}"