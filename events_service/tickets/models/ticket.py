from django.db import models

from . import Seat, TicketType, Timestamp


class Ticket(Timestamp):
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
        max_length=20,
        choices=STATUS,
        default=AVAILABLE,
    )
    seat = models.ForeignKey(Seat, on_delete=models.CASCADE)
    tickettype = models.ForeignKey(
        TicketType, related_name="tickettype_seats", on_delete=models.CASCADE)

    class Meta:
        unique_together = ('seat', 'tickettype')

    def __str__(self):
        return f"{self.seat} in {self.tickettype} {self.status}"
