# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from pollApp.models import Question

# Register your models here.
class QuestionAdmin(admin.ModelAdmin):
    fields = ['pub_date', 'question_text']

admin.site.register(Question, QuestionAdmin)