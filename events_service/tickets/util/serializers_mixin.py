from rest_framework import serializers

class CustomListSerializer(serializers.ListSerializer):
  def create(self, validated_data):
    objects = [self.child.create(attrs) for attrs in validated_data]
    return self.child.Meta.model.objects.bulk_create(objects)