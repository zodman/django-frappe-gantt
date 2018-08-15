from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static
from tasks.views import TaskView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # tenant app
    url(r'^$', TaskView.as_view()),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + staticfiles_urlpatterns()

urlpatterns += url(r'^admin/', include('loginas.urls')),
