from django.db import models
from django.contrib.auth.models import User

class Tenant(models.Model):
    name = models.CharField(max_length=200)
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)
    enabled = models.BooleanField()

    def __str__(self):
        return self.name

class TenantStudent(models.Model):
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    nim = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return f"{self.nim} - {self.name}"

class KeyboardShortcut(models.Model):
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    key = models.CharField(max_length=1)
    major_prefix = models.CharField(max_length=10, null=True, blank=True)
    year_prefix = models.CharField(max_length=10, null=True, blank=True)

    def __str__(self):
        return f"{self.name} on {self.tenant}"
