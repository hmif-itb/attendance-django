from django.db import models
from random import randint

# Create your models here.
class EventCategory(models.Model):
    category_name = models.CharField(max_length=200)

class Event(models.Model):
    name = models.CharField(max_length=200)
    date = models.DateTimeField('event date')
    category = models.ForeignKey(EventCategory, on_delete=models.PROTECT)
    code = models.PositiveIntegerField()

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if not self.code:
            is_unique = False
            while not is_unique:
                id = randint(100000, 999999)
                is_unique = Event.objects.filter(code=id).exists()
            self.code = id
        super(Event, self).save()