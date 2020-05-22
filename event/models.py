from django.db import models
from random import randint
from tenant.models import Tenant


class Event(models.Model):
    tenant = models.ForeignKey(Tenant, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200)
    date = models.DateTimeField('event date')
    checkin_open = models.BooleanField(default=True)
    code = models.PositiveIntegerField()

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if not self.code:
            self.code = randint(100000000, 999999999)
        super(Event, self).save()

    def regenerate_code(self):
        self.code = randint(100000000, 999999999)
        super(Event, self).save()

    def __str__(self):
        return self.name
