from rest_framework import serializers

from ..models import Event


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ('id', 'title', 'type', 'promoter',
                  'tags', 'venues', 'last_modified', 'created_at')
