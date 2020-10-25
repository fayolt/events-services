from django.db import models

from . import Event, Venue, Timestamp


class Date(Timestamp):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE)
    date = models.DateTimeField()

    def __str__(self):
        return (
            f"{self.event.__str__()} @ {self.venue.__str__()} "
            f"on { self.date.strftime('%Y-%m-%d %H:%M %Z')}"
        )
