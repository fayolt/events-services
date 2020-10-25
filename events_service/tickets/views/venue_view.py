from rest_framework import viewsets

from ..models import Venue
from ..serializers import VenueSerializer


class VenueViewSet(viewsets.ModelViewSet):
    queryset = Venue.objects.all()
    serializer_class = VenueSerializer
    # filter_backends = (filters.SearchFilter, )
    # search_fields = ('^short_name', '=abbreviation')
    # permission_classes = (permissions.IsAuthenticated, )
