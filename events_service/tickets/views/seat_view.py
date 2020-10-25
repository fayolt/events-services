from rest_framework import viewsets
from rest_framework import serializers

from ..models import Seat
from ..serializers import SeatSerializer
from ..util import ListCreateMixin


class SeatViewSet(ListCreateMixin, viewsets.ModelViewSet):
    serializer_class = SeatSerializer
    # filter_backends = (filters.SearchFilter, )
    # search_fields = ('^short_name', '=abbreviation')
    # permission_classes = (permissions.IsAuthenticated, )

    def get_queryset(self):
        return Seat.objects.filter(venue=self.kwargs['venue_id'])

    def create(self, request, *args, **kwargs):

        # Check if seats are saved under te right venue
        if not (
                isinstance(request.data, dict) and
                int(self.kwargs["venue_id"]) == self.request.data["venue"]):
            raise serializers.ValidationError(
                {"non_field_errors":
                    ["Trying to save seat under wrong venue"]},
                400)

        elif isinstance(request.data, list):
            for item in request.data:
                if int(self.kwargs["venue_id"]) == item["venue"]:
                    raise serializers.ValidationError(
                        {"non_field_errors":
                            ["Trying to save seat under wrong venue"]},
                        400)

        return super(SeatViewSet, self).create(request, *args, **kwargs)
