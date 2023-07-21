from rest_framework import serializers
from nota.models import Nota, NotaLineItem
from client.api.serializers import ClientSerializer
from client.models import Client

class NotaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nota
        fields = "__all__"
        read_only_fields = ['recipient_static_data', ]

    def create(self, validated_data):
        recipient = validated_data.pop('recipient', None)
        instance = self.Meta.model(**validated_data, recipient=recipient)
        instance.is_active = True
        if recipient is not None:
            instance.recipient_static_data = ClientSerializer(recipient).data
        instance.save()
        return instance


class NotaLineItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = NotaLineItem
        fields = "__all__"
