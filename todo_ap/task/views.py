from django.shortcuts import render, redirect
from django.http import HttpResponse
from task.models import Task
from task.models import Label
from task.forms import TaskForm
from task.forms import LabelForm

# tasks/  [GET, DELETE]
def index(request):

    if request.method == "GET":
        tasks_todo = Task.objects.filter(is_done=False)
        tasks_done = Task.objects.filter(is_done=True)

        context = {
        'tasks_todo': tasks_todo,
        'tasks_done': tasks_done,
        'form': TaskForm,
        }

        return render(request, "index.html", context)

    if request.method == "POST":

        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()

        return redirect('/')


# tasks/id/  [PUT, DELETE]
def task_detail_action(request, pk):


    task = Task.objects.get(id=pk)
    task.delete()
    return redirect('/')


def change_task_status(request, pk):
    task = Task.objects.get(id=pk)
    task.is_done = not task.is_done
    task.save()
    return redirect('/')


def label(request):

    if request.method == "GET":
        label_todo = Label.objects.filter(is_done=False)
        label_done = Label.objects.filter(is_done=True)

        context = {
        'label_todo': label_todo,
        'label_done': label_done,
        'form': LabelForm,
        }

        return render(request, "label.html", context)

    if request.method == "POST":

        form = LabelForm(request.POST)
        if form.is_valid():
            form.save()

        return redirect('/label')

def change_label_status(request, pk):
    label = Label.objects.get(id=pk)
    label.is_done = not label.is_done
    label.save()
    return redirect('/label')

def label_detail_action(request, pk):

    label = Label.objects.get(id=pk)
    label.delete()
    return redirect('/label')

# Create your views here.
