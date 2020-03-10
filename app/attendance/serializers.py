from rest_framework import serializers

from .models import Attendance, Attendee

class AttendeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendee
        fields = ['nim', 'name']

class AttendanceSerializer(serializers.ModelSerializer):
    attendee = AttendeeSerializer(many=False, read_only=True)

    class Meta:
        model = Attendance
        fields = ['id', 'attendee', 'created_at', 'updated_at']

class RecordAttendanceSerializer(serializers.Serializer):
    nim = serializers.CharField(max_length=8)