from rest_framework import routers
from . import viewsets
from django.urls import path, include

router_api = routers.DefaultRouter()
router_api.register(r'doctors', viewsets.DoctorViewSet, basename='doctors')

urlpatterns = [
    path('', include(router_api.urls)),
]