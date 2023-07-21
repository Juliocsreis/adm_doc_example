from rest_framework import viewsets
from address.models import Address
from . import serializers


class AddressViewSet(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = serializers.AddressSerializer


