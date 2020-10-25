import django_filters as filters

from ..models import Date


class CharArrayFilter(filters.BaseCSVFilter, filters.CharFilter):
    pass


class DateFilter(filters.FilterSet):
    date = filters.DateTimeFromToRangeFilter(field_name="date")
    event__title = filters.CharFilter(lookup_expr='icontains')
    event__type = filters.CharFilter(lookup_expr='icontains')
    event__promoter = filters.CharFilter(lookup_expr='icontains')
    event__tags = CharArrayFilter(method='filter_by_event_tags')
    venue__name = filters.CharFilter(lookup_expr='icontains')
    venue__address = filters.CharFilter(lookup_expr='icontains')
    venue__capacity = filters.NumericRangeFilter(field_name='venue__capacity')

    def filter_by_event_tags(self, queryset, name, value):
        lookup = "__".join([name, "overlap"])
        queryset = queryset.filter(**{lookup: value})
        return queryset

    class Meta:
        model = Date
        fields = []
