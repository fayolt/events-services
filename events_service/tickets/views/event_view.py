from rest_framework import viewsets, filters
from django_filters import rest_framework

from ..models import Event
from ..serializers import EventSerializer


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    # filter_backends = (rest_framework.DjangoFilterBackend, )
    # filter_class = EventFilter
    # permission_classes = (permissions.IsAuthenticated, )
