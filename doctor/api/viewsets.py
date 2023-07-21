from rest_framework import viewsets
from doctor.models import Doctor
from . import serializers


class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = serializers.DoctorSerializer
    authentication_classes = ()
    permission_classes = ()

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return self.queryset
        else:
            return self.queryset.filter(pk=user.pk)
