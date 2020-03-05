from django.db import models
from event.models import Event

# Create your models here.

class AttendeeMajor(models.Model):
    name = models.CharField(max_length=100)
    nim_prefix = models.CharField(max_length=3)
    keyboard_shortcut = models.CharField(max_length=1)

    def __str__(self):
        return f'{self.nim_prefix} - {self.name}'

class AttendeeYear(models.Model):
    name = models.CharField(max_length=100)
    nim_prefix = models.CharField(max_length=3)
    keyboard_shortcut = models.CharField(max_length=1)

    def __str__(self):
        return f'{self.nim_prefix} - {self.name}'

class Attendee(models.Model):
    nim = models.CharField(max_length=8, primary_key=True)
    name = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.nim} - {self.name}'

class Attendance(models.Model):
    event = models.ForeignKey(Event, on_delete=models.PROTECT)
    attendee = models.ForeignKey(Attendee, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.attendee.name} attending {self.event.name}'
