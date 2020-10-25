from rest_framework import viewsets, filters

from ..models import TicketType
from ..serializers import TicketTypeSerializer


class TicketTypeViewSet(viewsets.ModelViewSet):
    serializer_class = TicketTypeSerializer
    lookup_field = 'slug'
    lookup_value_regex = '[-\w]+'

    def get_queryset(self):
        return TicketType.objects.filter(date=self.kwargs['date_id'])
