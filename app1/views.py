from django.shortcuts import render,redirect
from .models import Task
from django.http import HttpResponse
# Create your views here.

def home(request):
    tasks = Task.objects.filter(is_completed=False).order_by('updated_at')
    return render(request,'app1/home.html',{'tasks':tasks})


def add_task(request):
    task = request.POST['task']
    Task.objects.create(task=task)
    return redirect('home')