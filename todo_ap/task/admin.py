from django.contrib import admin
from task.models import Task
from task.models import Label

# Register your models here.
admin.site.register(Task)
admin.site.register(Label)
