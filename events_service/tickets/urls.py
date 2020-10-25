from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views


router = DefaultRouter(trailing_slash=False)

router.register(r'venues', views.VenueViewSet)
router.register(r'events', views.EventViewSet)
router.register(r'dates', views.DateViewSet)
router.register(r'venues/(?P<venue_id>\d+)/seats',
                views.SeatViewSet, basename='venue-seats')
router.register(r'dates/(?P<date_id>\d+)/ticket-types',
                views.TicketTypeViewSet, basename='date-tickettype')
router.register(
    r'dates/(?P<date_id>\d+)/ticket-types/(?P<slug>[-\w]+)/tickets',
    views.TicketViewSet, basename='tickettype-ticket')


urlpatterns = [
    path('', include(router.urls))
]
