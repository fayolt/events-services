from rest_framework import serializers

from ..models import TicketType


class TicketTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TicketType
        fields = ('id', 'name', 'slug', 'quantity', 'price',
                  'date', 'last_modified', 'created_at')
        read_only_fields = ('slug', )
        lookup_field = 'slug'
