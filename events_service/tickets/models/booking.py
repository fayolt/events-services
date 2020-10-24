from django.db import models

from . import TicketTypeSeat, Timestamp

class Booking(Timestamp):
    # Booking status change
    # pending -> confirmed -> cancelled
    # pending -> timeout

    PENDING = 'PENDING'
    TIMEDOUT = 'TIMEDOUT'
    CONFIRMED = 'CONFIRMED'
    CANCELLED = 'CANCELLED'
    STATUS = (
        (PENDING, 'Pending'),
        (TIMEDOUT, 'Timedout'),
        (CONFIRMED, 'Confirmed'),
        (CANCELLED, 'Cancelled'),
    )
    status = models.CharField(
        max_length = 20,
        choices = STATUS,
        default = PENDING,
    )
    seat = models.OneToOneField(TicketTypeSeat, on_delete=models.CASCADE)