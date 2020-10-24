from rest_framework import viewsets

# filters, permissions
from ..models import Seat
from ..serializers import SeatSerializer
from ..util import ListCreateMixin

class SeatViewSet(ListCreateMixin, viewsets.ModelViewSet):
    def get_queryset(self):
        return Seat.objects.filter(venue=self.kwargs['venue_id'])
    
    # def create(self, request, *args, **kwargs):

    #     # Check if seats are saved under te right venue

    #     if isinstance(request.data, list):
    #         for item in request.data:
    #             item["project"] = project
    #     elif isinstance(request.data, dict) and self.kwargs["venue_id"] == self.request.data.venue.id:

    #     else:
    #         raise ValidationError("Invalid Input")

    #     return super(TaskCreateView, self).post(request, *args, **kwargs)
    serializer_class = SeatSerializer
    # filter_backends = (filters.SearchFilter, )
    # search_fields = ('^short_name', '=abbreviation')
    # permission_classes = (permissions.IsAuthenticated, )
