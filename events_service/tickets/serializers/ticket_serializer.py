from rest_framework import serializers

from ..models import Ticket
from ..util import CustomListSerializer


class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = ('id', 'seat', 'status', 'tickettype',
                  'last_modified', 'created_at')
        list_serializer_class = CustomListSerializer
