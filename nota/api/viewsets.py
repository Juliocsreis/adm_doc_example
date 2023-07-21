from rest_framework import viewsets
from nota.models import Nota, NotaLineItem
from . import serializers


class NotaViewSet(viewsets.ModelViewSet):
    queryset = Nota.objects.all()
    serializer_class = serializers.NotaSerializer


    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return self.queryset
        else:
            return self.queryset.filter(owner=user)


class NotaLineItemViewSet(viewsets.ModelViewSet):
    queryset = NotaLineItem.objects.all()
    serializer_class = serializers.NotaLineItemSerializer
