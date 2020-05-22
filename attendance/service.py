from django.db import transaction
from rest_framework import exceptions
from .models import Student, Attendance
from event.models import Event

class AttendanceService:
    @transaction.atomic
    def record_attendee(self, event_code, attendee_nim):
        event = Event.objects.get(code__exact = event_code)

        if (not event.checkin_open):
            raise exceptions.APIException(detail='Check in closed')

        attendance = Attendance.objects.create(
            event = event,
            attendee = attendee_nim
        )

        return attendance