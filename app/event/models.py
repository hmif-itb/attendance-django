from django.db import models
from random import randint

# Create your models here.
class EventCategory(models.Model):
    category_name = models.CharField(max_length=200)

    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name_plural = "Event categories"

class Event(models.Model):
    name = models.CharField(max_length=200)
    date = models.DateTimeField('event date')
    category = models.ForeignKey(EventCategory, on_delete=models.PROTECT)
    checkin_open = models.BooleanField(default=True)
    code = models.PositiveIntegerField()

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if not self.code:
            self.code = randint(100000, 999999)
        super(Event, self).save()

    def regenerate_code(self):
        self.code = randint(100000, 999999)
        super(Event, self).save()

    def __str__(self):
        return self.name