from django.contrib import admin


class TenantRestrictedAdmin:

	def get_queryset(self, request, *args, **kwargs):
		qs = super().get_queryset(request, *args, **kwargs)
		if request.tenant:
			qs = qs.filter(tenant=tenant)
		return qs

	def save_model(self, request, obj, form, change):
		if request.tenant:
			obj.tenant = request.tenant
			obj.save()
			super().save_model(request, obj, form, change)
