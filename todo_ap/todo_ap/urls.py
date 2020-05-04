
from django.contrib import admin
from django.urls import path

from task.views import index

from task.views import task_detail_action

from task.views import change_task_status

from task.views import label

from task.views import change_label_status

from task.views import label_detail_action

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('tasks/<int:pk>/', task_detail_action),
    path('tasks/status/<int:pk>/', change_task_status),
    path('label/', label),
    path('label/status/<int:pk>/', change_label_status),
    path('label/detail/<int:pk>/', label_detail_action),
]
