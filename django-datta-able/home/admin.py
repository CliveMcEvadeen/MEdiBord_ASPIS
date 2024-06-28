from django.contrib import admin

from django.apps import apps
# from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Student)
admin.site.register(Subject)
admin.site.register(StudentSubject)
admin.site.register(Marks)

app_models = apps.get_app_config('home').get_models()
for model in app_models:
    try:    

        admin.site.register(model)

    except Exception:
        pass
