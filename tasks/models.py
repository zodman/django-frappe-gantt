# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from treebeard.mp_tree import MP_Node
from django.db import models
from django_model_to_dict.mixins import ToDictMixin


class Task(MP_Node, ToDictMixin):
    name = models.CharField(max_length=100)
    start = models.DateField()
    end = models.DateField()
    progress = models.PositiveIntegerField()

    def __unicode__(self):
        return u"{}".format(self.name)
