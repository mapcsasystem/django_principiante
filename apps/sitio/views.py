from django.shortcuts import render
from .models import Project, Task
# Create your views here.


def index(request):
    vars = {
        'title': 'PRINCIPIANTE'
    }
    return render(request, 'index.html', vars)


def projects(request):
    projects = Project.objects.all()
    context = {
        'projects': projects
    }
    return render(request, 'projects.html', context)


def tasks(request):
    tasks = Task.objects.all()
    context = {
        'tasks': tasks
    }
    return render(request, 'tasks.html', context)
