from rest_framework import serializers

from ..models import Date
from . import EventSerializer, VenueSerializer


class DateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Date
        fields = ('event', 'venue', 'date', )