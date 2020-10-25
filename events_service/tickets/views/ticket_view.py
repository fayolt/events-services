from rest_framework import viewsets, filters

from ..models import Ticket
from ..serializers import TicketSerializer
from ..util import ListCreateMixin


class TicketViewSet(ListCreateMixin, viewsets.ModelViewSet):
    serializer_class = TicketSerializer

    def get_queryset(self):
        return Ticket.objects.filter(
            tickettype__date=self.kwargs['date_id'],
            tickettype__slug=self.kwargs['slug']
        )

    # ensure that url param slug and ticket type id refer to same object
