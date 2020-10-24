from rest_framework import serializers

from ..models import TicketTypeSeat

class TicketTypeSeatSerializer(serializers.ModelSerializer):
  class Meta:
    model = TicketTypeSeat
    fields = ('seat', 'status', 'ticket_type', 'last_saved', 'created_at', )
    read_only_fields = ('last_saved', 'created_at')