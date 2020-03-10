from django.db import transaction
from rest_framework import exceptions
from .models import Attendee, Attendance
from event.models import Event

class AttendanceService:
    @transaction.atomic
    def record_attendee(self, event_code, attendee_nim):
        event = Event.objects.get(code__exact = event_code)

        if (not event.checkin_open):
            raise exceptions.APIException(detail='Check in closed')

        try:
            attendee = Attendee.objects.get(nim__exact = attendee_nim)
        except Attendee.DoesNotExist:
            attendee = Attendee.objects.create(
                nim = attendee_nim,
                name = attendee_nim
            )

        attendance = Attendance.objects.create(
            event = event,
            attendee = attendee
        )

        return attendance