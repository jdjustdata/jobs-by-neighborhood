# # -*- coding: utf-8 -*-
# from __future__ import unicode_literals
#
# from django.contrib.postgres.fields import JSONField
# from django.contrib.auth.models import User
# from .pagelists.components import COMPONENT_CHOICES
# from .pagelists.content import CONTENT_CHOICES
# from ..languages.models import LANGUAGE_CODE_CHOICES, SUPPORTED_LANGUAGES, DEFAULT_LANGUAGE
#
# from django.db import models
#
# class PageResources(models.Model):
#     SUPPORTED_LANGUAGES = SUPPORTED_LANGUAGES
#
#     component = models.CharField(max_length=2, choices=COMPONENT_CHOICES)
#     content_type = models.CharField(max_length=2, choices=CONTENT_CHOICES)
#     page_name = models.CharField(max_length=100)
#     data = JSONField()
#     language = models.CharField(max_length=2, choices=LANGUAGE_CODE_CHOICES, default=DEFAULT_LANGUAGE)
#     language_validated = models.BooleanField(default=False)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#     created_by = models.ForeignKey(User, on_delete=models.PROTECT, related_name="PagesCreated")
#     updated_by = models.ForeignKey(User, on_delete=models.PROTECT, related_name="PagesUpdated")
