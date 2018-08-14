from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Tenant, TenantUser


class TenantRestrictedAdmin:
	exclude = ("tenant", )

	def get_queryset(self, request, *args, **kwargs):
		qs = super().get_queryset(request, *args, **kwargs)
		if request.tenant:
			qs = qs.filter(tenant=request.tenant)
		return qs

	def save_model(self, request, obj, form, change):
		if request.tenant:
			obj.tenant = request.tenant
			obj.save()
			super().save_model(request, obj, form, change)


@admin.register(TenantUser)
class TenantUserAdmin(admin.ModelAdmin):
	list_display = ("tenant", "user")
	search_fields = ("tenant__subdomain", "user__username")
	autocomplete_fields  = [ "user","tenant"]

@admin.register(Tenant)
class TenantAdmin(admin.ModelAdmin):
	search_fields =["subdomain"]
	

