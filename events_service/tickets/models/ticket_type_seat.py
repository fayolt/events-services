from django.db import models

from . import Seat, TicketType, Timestamp

class TicketTypeSeat(Timestamp):
    # Seat status change 
    # available -> reserved -> booked -> available
    # available -> reserved -> available
    AVAILABLE = 'AVAILABLE'
    RESERVED = 'RESERVED'
    BOOKED = 'BOOKED'
    STATUS = (
        (AVAILABLE, 'Available'),
        (RESERVED, 'Reserved'),
        (BOOKED, 'Booked'),
    )
    status = models.CharField(
        max_length = 20,
        choices = STATUS,
        default = AVAILABLE,
    )
    seat = models.OneToOneField(Seat, on_delete=models.CASCADE, primary_key=True)
    ticket_type = models.ForeignKey(TicketType, related_name="ticket_type_seats", on_delete=models.CASCADE)