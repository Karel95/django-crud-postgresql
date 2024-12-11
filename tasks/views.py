from django.shortcuts import render, redirect
from .models import Task

# Create your views here.
def list_tasks(request):
  tasks = Task.objects.all()
  return render(request, 'list_tasks.html', {'tasks': tasks})

def create_task(request):
  task = Task(title=request.POST['title'], description=request.POST['description'])
  task.save()
  return redirect('/tasks/')

def delete_task(request, id):
  task = Task.objects.get(id=id)
  task.delete()
  return redirect('/tasks/')

# def update_task(request):
#   task = Task.objects.get(id=request.POST['id'])
#   task.title = request.POST['title']
#   task.description = request.POST['description']
#   task.save()
#   return redirect('/tasks/')
