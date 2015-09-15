#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models
from jsonfield.fields import JSONField


class ImpApply(models.Model):
    name = models.CharField(max_length=50, verbose_name=u'名称')
    json = JSONField(default={"test": 1, "fields": {"type": "text", "default": ""}})
    state = models.BooleanField(verbose_name=u'实施完成', default=False)
    notes = models.TextField(blank=True, verbose_name=u'备注')
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = u'实施申请'
        verbose_name_plural = u'实施申请列表'
        ordering = ['-timestamp']
