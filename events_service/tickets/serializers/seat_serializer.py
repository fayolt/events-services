from rest_framework import serializers
from ..models import Seat
from ..util import CustomListSerializer


class SeatSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Seat
        fields = ('number', 'row', 'gate', 'state', 'section', 'venue', 'last_saved', 'created_at', )
        read_only_fields = ('last_saved', 'created_at')
        list_serializer_class = CustomListSerializer