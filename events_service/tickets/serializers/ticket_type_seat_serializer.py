from rest_framework import serializers

from ..models import TicketTypeSeat
from ..util import CustomListSerializer


class TicketTypeSeatSerializer(serializers.ModelSerializer):
    class Meta:
        model = TicketTypeSeat
        fields = ('seat', 'status', 'ticket_type',
                  'last_modified', 'created_at')
        read_only_fields = ('last_modified', 'created_at')
        list_serializer_class = CustomListSerializer
