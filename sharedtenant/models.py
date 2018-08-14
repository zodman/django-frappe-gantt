from django.db import models

class Tenant(models.Model):
	subdomain = models.CharField(max_length=50)

	def __str__(self):
		return self.subdomain


class TenantMix(models.Model):
	tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)

	class Meta:
		abstract = True
