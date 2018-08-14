from .models import Tenant 
from django.core import exceptions
from .exceptions import Http401

class SharedTenantMiddleware:
	
	def __init__(self, get_response):
		self.get_response = get_response

	def __call__(self, request):
		
		host = request.get_host().split(":")[0].lower()
		subdomain = host.split('.')[0].lower()
		try:
			tenant = Tenant.objects.get(subdomain=subdomain)
		except Tenant.DoesNotExist:
			tenant = None

		request.tenant = tenant

		if "admin" in request.path:
			user = request.user
			tenant_users = tenant.tenantuser_set.filter(user=user)
			if not tenant_users.exists():
				raise Http401

		response = self.get_response(request)
		return response