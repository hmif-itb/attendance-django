from django.db import models
from event.models import Event


class Student(models.Model):
    nim = models.CharField(max_length=20, primary_key=True)
    name = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.nim} - {self.name}'


class Attendance(models.Model):
    event = models.ForeignKey(Event, on_delete=models.PROTECT)
    attendee = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.attendee} attending {self.event.name}'
