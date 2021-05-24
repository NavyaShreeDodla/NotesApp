from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from .forms import *
# Create your views here.
def index(request):
    tasks=task.objects.all()
    form = TaskForm()
    if(request.method =='POST'):
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    return render(request,'list.html',{'tasks':tasks,'form':form})
def update(request,pk):
    tasks=task.objects.get(id=pk)
    form = TaskForm(instance=tasks)
    if(request.method == 'POST'):
        form = TaskForm(request.POST, instance=tasks)
        if form.is_valid():
            form.save()
        return redirect('/')
    return render(request, 'update.html',{'form':form})
def delete(request,pk):
    item = task.objects.get(id=pk)
    if(request.method == 'POST'):
        item.delete()
        return redirect('/')
    return render(request, 'delete.html',{'item':item})