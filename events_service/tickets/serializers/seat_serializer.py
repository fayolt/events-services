from rest_framework import serializers

from ..models import Seat
from ..util import CustomListSerializer


class SeatSerializer(serializers.ModelSerializer):

    class Meta:
        model = Seat
        fields = ('id', 'number', 'row', 'gate', 'state', 'section',
                  'venue', 'last_modified', 'created_at', )
        read_only_fields = ('id', 'last_modified', 'created_at')
        list_serializer_class = CustomListSerializer
