from django.db import models

from . import Timestamp, Venue
from .choices import SeatState

class Seat(Timestamp):
    """
    docstring
    """
    number = models.PositiveIntegerField()
    row = models.PositiveIntegerField()
    gate = models.CharField(max_length=20)
    state = models.CharField(
        max_length = 20,
        choices = [(state, state.value) for state in SeatState],
        default = SeatState.GOOD,
    )
    section = models.CharField(max_length=20)
    venue = models.ForeignKey(Venue, related_name="venue_seats", on_delete=models.CASCADE)