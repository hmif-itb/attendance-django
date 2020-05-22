from rest_framework import serializers

from .models import Event
from tenant.serializers import TenantSerializer

class EventSerializer(serializers.ModelSerializer):
    tenant = TenantSerializer()
    class Meta:
        model = Event
        fields = ['id', 'name', 'date', 'checkin_open', 'code', 'tenant']
