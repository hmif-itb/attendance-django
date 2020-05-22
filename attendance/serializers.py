from rest_framework import serializers
from .models import Attendance, Student


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['nim', 'name']


class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = ['id', 'student', 'created_at', 'updated_at']


class RecordAttendanceSerializer(serializers.Serializer):
    nim = serializers.CharField(max_length=8)
