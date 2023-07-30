from django.shortcuts import render,redirect
from .models import TaskModel
from django.contrib import messages
from .forms import TaskForm
from django.views.generic import DetailView,UpdateView,ListView,DeleteView,CreateView
from django.urls import reverse,reverse_lazy

# Create your views here.
def taskdetails(request):
    task_list=TaskModel.objects.all().order_by('priority')
    if request.method=="POST":
        task=request.POST.get('task',None)
        priority=request.POST.get('priority',None)
        date=request.POST.get('date',None)
        if task and priority:
            add_task=TaskModel(task=task,priority=priority,date=date)
            add_task.save()
            return redirect("/")
        else:
            messages.error(request,'Pls enter valid data')
    return render(request,"index.html",{'task_list':task_list})

def deletetask(request,slug):
    TaskModel.objects.filter(id=slug).delete()
    return redirect('/')

def update(request,slug):
    update_task=TaskModel.objects.filter(id=slug).first()
    if request.method=="POST":
        print("aaaaaa")
        form=TaskForm(request.POST or None,instance=update_task)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form=TaskForm(instance=update_task)
    return render(request,"update.html",{'form':form})


# ==========================================================
class TodoCreateView(CreateView):
    model = TaskModel
    form_class = TaskForm
    template_name = 'create_view.html'
    success_url = reverse_lazy('task:create_view')

class TodoListView(ListView):
    context={}
    model=TaskModel
    template_name = "list_view.html"
    context_object_name ='task_list'
    
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['task_list']='task_list'
    #     return context
    
class TodoDetailView(DetailView):
    model=TaskModel
    template_name="details.html"
    context_object_name='task_list'
    
class TodoUpdateView(UpdateView):
    model=TaskModel
    form_class = TaskForm
    template_name="update_view.html"
    # context_object_name='task_list'
    # fields=('task','priority','date')

    def get_success_url(self):
        return reverse_lazy('task:detail_view', kwargs={'pk': self.object.id})
    
class TodoDeleteView(DeleteView):
    model=TaskModel
    template_name="delete.html"
    success_url=reverse_lazy('task:list_view')