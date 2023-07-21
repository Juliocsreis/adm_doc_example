from rest_framework import routers
from . import viewsets
from django.urls import path, include

router_api = routers.DefaultRouter()
router_api.register(r'notas', viewsets.NotaViewSet, basename='notas')
router_api.register(r'notas_line_item', viewsets.NotaLineItemViewSet, basename='notas_line_item')

urlpatterns = [
    path('', include(router_api.urls)),
]