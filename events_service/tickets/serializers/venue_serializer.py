from rest_framework import serializers
from ..models import Venue

class VenueSerializer(serializers.ModelSerializer):
    # method = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = Venue
        fields = ('id', 'name', 'address', 'capacity', 'events', 'created_at', )