from rest_framework import viewsets, filters
from django_filters import rest_framework

# filters, permissions
from ..models import Event
from ..serializers import EventSerializer

# from ..filters import EventFilter

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    # filter_backends = (rest_framework.DjangoFilterBackend, )
    # filter_class = EventFilter
    # permission_classes = (permissions.IsAuthenticated, )
