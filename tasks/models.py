# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from treebeard.mp_tree import MP_Node
from django.db import models
from django_model_to_dict.mixins import ToDictMixin
from sharedtenant.models import TenantMix


class Project(ToDictMixin, TenantMix, models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.__unicode__()

    def __unicode__(self):
        return u"{}".format(self.name)

class Task(MP_Node, ToDictMixin, TenantMix):
    name = models.CharField(max_length=100)
    start = models.DateField()
    end = models.DateField()
    progress = models.PositiveIntegerField(default=0)
    custom_class = models.CharField(max_length=20, null=True, blank=True)
    project = models.ForeignKey("Project", related_name="tasks", null=True,
                                blank=True,  on_delete=models.CASCADE)

    def __str__(self):
        return self.__unicode__()

    def __unicode__(self):
        return u"{}".format(self.name)
