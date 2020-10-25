from rest_framework import viewsets
from django_filters import rest_framework

from ..models import Date
from ..serializers import DateSerializer
from ..filters import DateFilter


class DateViewSet(viewsets.ModelViewSet):
    queryset = Date.objects.all()
    serializer_class = DateSerializer
    filter_backends = (rest_framework.DjangoFilterBackend, )
    filter_class = DateFilter
