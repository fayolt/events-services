from rest_framework import viewsets

# filters, permissions
from ..models import Date
from ..serializers import DateSerializer

class DateViewSet(viewsets.ModelViewSet):
    queryset = Date.objects.all()
    serializer_class = DateSerializer