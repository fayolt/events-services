from rest_framework import viewsets, filters

from ..models import TicketType
from ..serializers import TicketTypeSerializer


class TicketTypeViewSet(viewsets.ModelViewSet):
    serializer_class = TicketTypeSerializer
    def get_queryset(self):
        print(self.basename)
        return TicketType.objects.filter(date=self.kwargs['date_id'])
