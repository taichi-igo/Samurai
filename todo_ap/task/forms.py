from django import forms
from task.models import Task
from task.models import Label

class TaskForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = '__all__'


class LabelForm(forms.ModelForm):

    class Meta:
        model = Label
        fields = '__all__'
