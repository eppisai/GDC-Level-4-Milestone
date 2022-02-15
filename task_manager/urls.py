from django.contrib import admin
from django.urls import path

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

tasks = []
completed = []

def tasks_view(request):
    return render(request,"tasks.html",{"tasks":tasks})

def add_task_view(request):
    task_value = request.GET.get("task")
    tasks.append(task_value)
    return HttpResponseRedirect("/tasks")

def delete_task_view(request, index):
    del tasks[index-1]
    return HttpResponseRedirect("/tasks")

def complete_task_view(request, index):
    thisTask = tasks[index-1]
    completed.append(thisTask)
    del tasks[index-1]
    return HttpResponseRedirect("/tasks")

def completed_tasks_view(request):
    return render(request,"display.html",{"completed":completed})

def all_tasks_view(request):
    return render(request,"display.html",{"completed":completed, "tasks":tasks})

urlpatterns = [
    path('',tasks_view),
    path("admin/", admin.site.urls),
    path('tasks/',tasks_view),
    path('add-task/', add_task_view),
    path("delete-task/<int:index>/", delete_task_view),
    path("complete_task/<int:index>/", complete_task_view),
    path("completed_tasks/", completed_tasks_view),
    path("all_tasks/", all_tasks_view)
]
