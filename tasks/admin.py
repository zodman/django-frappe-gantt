# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.urls import reverse_lazy
from django.utils.safestring import mark_safe

from treebeard.admin import TreeAdmin
from treebeard.forms import movenodeform_factory

from tasks.models import Task, Project
from sharedtenant.admin import TenantRestrictedAdmin


class AdminTask(TreeAdmin, TenantRestrictedAdmin):
    list_display = ("name", "progress", "start","end")
    list_editable = ("progress", 'start','end',)
    list_select_related = ("project",)
    list_filter = ("project",)
    form = movenodeform_factory(Task)

admin.site.register(Task, AdminTask)


class AdminProject(admin.ModelAdmin, TenantRestrictedAdmin):
	list_display = ("name", "show_tasks")

	def show_tasks(self, obj):
		urlpath = reverse_lazy("admin:tasks_task_changelist")
		urlpath +="?project__id__exact={}".format(obj.id)
		u = """
		<a href='{}'>Tasks</a>
		""".format(urlpath)
		return mark_safe(u)
	


admin.site.register(Project, AdminProject)
