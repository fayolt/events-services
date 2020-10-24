from rest_framework import viewsets, filters
# from django_filters import rest_framework

# filters, permissions
from ..models import TicketType
from ..serializers import TicketTypeSerializer

# from ..filters import EventFilter

class TicketTypeViewSet(viewsets.ModelViewSet):
    serializer_class = TicketTypeSerializer
    def get_queryset(self):
        print(self.basename)
        return TicketType.objects.filter(date=self.kwargs['date_id'])
    # filter_backends = (rest_framework.DjangoFilterBackend, )
    # filter_class = EventFilter
    # permission_classes = (permissions.IsAuthenticated, )
