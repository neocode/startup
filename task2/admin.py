__author__ = 'alex'

from django.contrib import admin

from task2.models import model_list
for model in model_list:
    admin.site.register(model)