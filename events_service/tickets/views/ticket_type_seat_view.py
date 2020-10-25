from rest_framework import viewsets, filters

from ..models import TicketTypeSeat
from ..serializers import TicketTypeSeatSerializer
from ..util import ListCreateMixin


class TicketTypeSeatViewSet(ListCreateMixin, viewsets.ModelViewSet):
    serializer_class = TicketTypeSeatSerializer

    def get_queryset(self):
        return TicketTypeSeat.objects.filter(
            tickettype__date=self.kwargs['date_id'],
            tickettype__slug=self.kwargs['slug']
        )
