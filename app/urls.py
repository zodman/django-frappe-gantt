from django.conf.urls import url
from django.contrib import admin
from django.views.generic import TemplateView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static
from tasks.models import Task
import json 

class TaskView(TemplateView):
    template_name ="index.html"
    def process(self, t):
        task = t.to_dict()
        for i in ('path', 'depth', 'path', 'numchild'):
            if i in task:
                del task[i]
        task['id'] = str(task['id'])
        childrens = [c.id for c in t.get_children()]
        task["dependencies"] = ",".join([str(i) for i in childrens])
        return task
    def get_context_data(self, **kwargs):
        ctx = super(TaskView, self).get_context_data(**kwargs)
        tasks = Task.objects.all()

        ctx["tasks"] = json.dumps([ self.process(t) for t in tasks])    
        return ctx


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', TaskView.as_view()),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + staticfiles_urlpatterns()
