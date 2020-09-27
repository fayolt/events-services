from rest_framework import serializers
from ..models import Event

class EventSerializer(serializers.ModelSerializer):
    # id = serializers.IntegerField(required=False)
    # method = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = Event
        fields = ('id', 'title', 'type', 'promoter', 'tags', 'created_at', )