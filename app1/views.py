from django.shortcuts import render,redirect,get_object_or_404
from .models import Task
from django.http import HttpResponse
# Create your views here.

def home(request):
    tasks = Task.objects.filter(is_completed=False).order_by('-updated_at')
    completedTask = Task.objects.filter(is_completed = True)
    context ={
        'tasks':tasks,
        'completedTask':completedTask
    }
    return render(request,'app1/home.html',context)


def add_task(request):
    task = request.POST['task']
    Task.objects.create(task=task)
    return redirect('home')


def mark_as_done(request,pk):
    task = get_object_or_404(Task,pk=pk)
    task.is_completed = True
    task.save()
    return redirect('home')


def mark_as_undone(request,pk):
    task = get_object_or_404(Task,pk=pk)
    task.is_completed = False
    task.save()
    return redirect('home')

def delete(request,pk):
    task = get_object_or_404(Task,pk=pk)
    task.delete()
    return redirect('home')

def edit(request,pk):
    task = get_object_or_404(Task,pk=pk)
    if request.method == 'POST':
        new_task = request.POST['task']
        task.task = new_task
        task.save()
        return redirect('home')
    else:
        context = {
            'task':task
        }
    return render(request,'app1/edit_task.html',context)