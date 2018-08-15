from .models import Tenant
from django.core import exceptions
from django.http import Http404

class SharedTenantMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        host = request.get_host().split(":")[0].lower()
        subdomain = host.split('.')[0].lower()
        try:
            tenant = Tenant.objects.get(subdomain=subdomain)
        except Tenant.DoesNotExist:
            tenant = Tenant.objects.none()

        request.tenant = tenant

        if "admin/tasks" in request.path and request.tenant and \
            request.user.is_authenticated:
            user = request.user
            tenant_users = tenant.tenantuser_set.filter(user=user)
            if not tenant_users.exists() and not request.user.is_superuser:
                raise Http404('Not allowed user')

        response = self.get_response(request)
        return response
