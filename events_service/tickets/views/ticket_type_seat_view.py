from rest_framework import viewsets, filters

from ..models import TicketTypeSeat
from ..serializers import TicketTypeSeatSerializer


class TicketTypeSeatViewSet(viewsets.ModelViewSet):
    serializer_class = TicketTypeSeatSerializer
    def get_queryset(self):
        print(self.basename)
        return TicketTypeSeat.objects.filter(ticket_type__name=self.kwargs['slug'].replace('-', ' '))
