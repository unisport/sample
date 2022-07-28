from django.contrib import admin
from django.contrib.admin.sites import AlreadyRegistered
from django.apps import apps

models = apps.get_models()

for model in models:
    try:
        admin.site.register(model)
    except AlreadyRegistered:
        pass
