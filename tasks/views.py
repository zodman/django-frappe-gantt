# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.views.generic import TemplateView
from tasks.models import Task, Project
import json 

class TaskView(TemplateView):
    template_name ="index.html"
    def process(self, t):
        task = t.to_dict()
        for i in ('path', 'depth', 'path', 'numchild','project'):
            if i in task:
                del task[i]
        task['id'] = str(task['id'])
        childrens = [c.id for c in t.get_children()]
        task["dependencies"] = ",".join([str(i) for i in childrens])
        return task

    def get_context_data(self, **kwargs):
        ctx = super(TaskView, self).get_context_data(**kwargs)
        id = self.request.GET.get("id",None)

        if not id:
            tasks = Task.objects.none()
        else:
            tasks = Task.objects.filter(project__id=id)

        ctx["id"] = id
        ctx["projects"] = Project.objects.all()
        ctx["tasks_count"] = tasks.count()
        ctx["tasks"] = json.dumps([ self.process(t) for t in tasks])    

        return ctx

