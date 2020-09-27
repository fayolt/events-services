from django.db import models

from . import Date, Timestamp

class TicketType(Timestamp):
    """
    docstring
    """
    name = models.CharField(max_length=20)
    capacity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=11, decimal_places=2)
    date = models.ForeignKey(Date, related_name="ticket_types", on_delete=models.CASCADE)