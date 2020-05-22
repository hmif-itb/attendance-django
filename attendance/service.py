from django.db import transaction
from rest_framework import exceptions
from .models import Student, Attendance
from event.models import Event
from tenant.models import TenantStudent

class AttendanceService:

    @transaction.atomic
    def record_attendee(self, event_code, attendee_nim, ignore_attendee = False):
        event = Event.objects.get(code__exact = event_code)

        if not event.checkin_open:
            raise exceptions.PermissionDenied(detail='Check in closed')

        if not ignore_attendee:
            attendee = self.get_attendee(event.tenant, attendee_nim)

            if not attendee:
                raise exceptions.NotFound(detail='Attendee does not exist in tenant')

        attendance = Attendance.objects.create(
            event = event,
            attendee = attendee_nim
        )

        return attendance

    def get_attendee(self, tenant, attendee_nim):
        student = Student.objects.filter(nim__exact = attendee_nim).first()

        if not student:
            student = TenantStudent.objects.filter(tenant = tenant, nim__exact = attendee_nim)

        return student
