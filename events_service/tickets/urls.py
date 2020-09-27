from django.urls import path, include
from rest_framework.routers import DefaultRouter
from django.conf import settings
from . import views


# class CustomRouter(DefaultRouter):
#     def __init__(self, *args, **kwargs): 
#         super(DefaultRouter, self).__init__(*args, **kwargs) 
#         self.trailing_slash = '/?'

router = DefaultRouter()
router.register(r'events', views.EventViewSet)


urlpatterns = [
    path('', include(router.urls)),
]