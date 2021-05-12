from django.shortcuts import render,redirect
from . models import Task
from . forms import Todoforms
from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy

# Create your views here.

class Task_lv(ListView):
    model = Task
    template_name = 'task_view.html'
    context_object_name = 'obj'

class Task_dv(DetailView):
    model=Task
    template_name = 'detail.html'
    context_object_name = 'i'

class Task_uv(UpdateView):
    model = Task
    template_name = 'update.html'
    context_object_name = 'task'
    fields = ('name','priority','date')
    def get_success_url(self):
        return reverse_lazy('conobdetail',kwargs={'pk':self.object.id})

class Task_delv(DeleteView):
    model = Task
    template_name = 'delete.html'
    context_object_name = 'task'
    success_url = reverse_lazy('conobtask')

def task_view(request):
    if request.method=='POST':
        name=request.POST.get('name')
        priority=request.POST.get('priority')
        date=request.POST.get('date')
        obj=Task(name=name,priority=priority,date=date)
        obj.save()
    obj1=Task.objects.all()
    return render(request,'task_view.html',{'obj':obj1})

def delete(request,task_id):
    task=Task.objects.get(id=task_id)
    if request.method=='POST':
        task.delete()
        return redirect('/')
    return render(request,'delete.html',{'task':task})

def update(request,task_id):
    task=Task.objects.get(id=task_id)
    form=Todoforms(request.POST or None,instance=task)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'task':task,'form':form})