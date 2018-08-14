from .models import Tenant 

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
		response = self.get_response(request)
		return response