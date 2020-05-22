from rest_framework.response import Response
from rest_framework import generics
from .serializers import AttendanceSerializer, RecordAttendanceSerializer
from .models import Attendance
from .service import AttendanceService

# Create your views here.
class AttendanceView(generics.ListAPIView):
    serializer_class = AttendanceSerializer

    def get_queryset(self):
        return Attendance.objects.filter(event__code = self.kwargs['code']).order_by('-created_at')


class RecordAttendanceView(generics.CreateAPIView):
    serializer_class = RecordAttendanceSerializer

    def post(self, request, format=None, *args, **kwargs):
        request_serializer = RecordAttendanceSerializer(data=request.data)
        request_serializer.is_valid(raise_exception=True)

        ignore_attendee = request.data['ignore_attendee'] if 'ignore_attendee' in request.data else False
        attendance = AttendanceService().record_attendee(self.kwargs['code'], request.data['nim'], ignore_attendee)
        response_serializer = AttendanceSerializer(attendance)
        return Response(data=response_serializer.data)


class DestroyAttendanceView(generics.DestroyAPIView):
    serializer_class = AttendanceSerializer
    def get_queryset(self):
        return Attendance.objects.filter(event__code = self.kwargs['code'])
