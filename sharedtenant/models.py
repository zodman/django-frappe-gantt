from django.db import models
from django.contrib.auth.models import User


class Tenant(models.Model):
    subdomain = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.subdomain


class TenantUser(models.Model):
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class TenantMix(models.Model):
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)

    class Meta:
        abstract = True
