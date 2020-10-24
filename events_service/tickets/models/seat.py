from django.db import models

from . import Timestamp, Venue

class Seat(Timestamp):
    GOOD = 'GOOD'
    WEARY = 'WEARY'
    BROKEN = 'BROKEN'
    STATE = (
        (GOOD, 'Good'),
        (WEARY, 'Weary'),
        (BROKEN, 'Broken'),
    )
    number = models.PositiveIntegerField()
    row = models.PositiveIntegerField()
    gate = models.CharField(max_length=20)
    state = models.CharField(
        max_length = 20,
        choices = STATE,
        default = GOOD,
    )
    section = models.CharField(max_length=20)
    venue = models.ForeignKey(Venue, related_name="venue_seats", on_delete=models.CASCADE)