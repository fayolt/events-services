from django.db import models

from . import Seat, TicketType, Timestamp
from .choices import TicketTypeSeatStatus

class TicketTypeSeat(Timestamp):
    """
    docstring
    """
    status = models.CharField(
        max_length = 20,
        choices = [(status, status.value) for status in TicketTypeSeatStatus],
        default = TicketTypeSeatStatus.AVAILABLE,
    )
    seat = models.OneToOneField(Seat, on_delete=models.CASCADE, primary_key=True)
    ticket_type = models.ForeignKey(TicketType, related_name="ticket_type_seats", on_delete=models.CASCADE)