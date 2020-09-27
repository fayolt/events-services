from django.db import models

from . import TicketTypeSeat, Timestamp
from .choices import BookingStatus

class Booking(Timestamp):
    """
    docstring
    """
    status = models.CharField(
        max_length = 20,
        choices = [(status, status.value) for status in BookingStatus],
        default = BookingStatus.PENDING,
    )
    seat = models.OneToOneField(TicketTypeSeat, on_delete=models.CASCADE)