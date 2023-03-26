from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse

from . models import todo
from . forms import todoform

def add(request):
    if request.method=='POST':
        name=request.POST.get('task')
        priority=request.POST.get('priority')
        date=request.POST.get('date')
        task=todo(name=name,priority=priority,date=date)
        task.save()
    task1=todo.objects.all()
    return render(request,'index.html',{'task':task1})
def delete(request,taskid):
    task=todo.objects.get(id=taskid)
    if request.method == 'POST':
        task.delete()
        return redirect('/')
    return render (request,'delete.html')
def update(request,id):
    task=todo.objects.get(id=id)
    form=todoform(request.POST or None ,instance=task)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'update.html',{'form':form,'task':task})