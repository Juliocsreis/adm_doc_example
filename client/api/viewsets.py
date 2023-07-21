from rest_framework import viewsets
from client.models import Client
from . import serializers


class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = serializers.ClientSerializer


