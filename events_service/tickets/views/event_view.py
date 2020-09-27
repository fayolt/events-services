from rest_framework import viewsets

# filters, permissions
from ..models import Event
from ..serializers import EventSerializer

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    # filter_backends = (filters.SearchFilter, )
    # search_fields = ('^short_name', '=abbreviation')
    # permission_classes = (permissions.IsAuthenticated, )
