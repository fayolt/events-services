from rest_framework import serializers

from ..models import Venue


class VenueSerializer(serializers.ModelSerializer):

    class Meta:
        model = Venue
        fields = ('id', 'name', 'address', 'capacity',
                  'events', 'last_modified', 'created_at')
        read_only_fields = ('id', 'last_modified', 'created_at')
