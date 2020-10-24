from django.urls import path, include
from rest_framework.routers import DefaultRouter
# from rest_framework_nested import routers
from . import views


router = DefaultRouter(trailing_slash=False)

router.register(r'venues', views.VenueViewSet)
router.register(r'events', views.EventViewSet)
router.register(r'dates', views.DateViewSet)
router.register(r'venues/(?P<venue_id>\d+)/seats', views.SeatViewSet, basename='venue-seats')
# venues_router = routers.NestedDefaultRouter(router, r'venues', lookup='venue')
# venues_router.register(r'seats', views.SeatViewSet, basename='venue-seats')






urlpatterns = [
    path('', include(router.urls))
]