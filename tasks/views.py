from django.shortcuts import render,redirect
from .models import TaskModel
from .forms import TaskForm
from django.contrib.auth.decorators import login_required
from django.utils.timezone import datetime




# Create your views here.

def added_task(request):   
    if request.user.is_authenticated:
        user = request.user
        # print(user)                  
        form = TaskForm(request.POST)
        if form.is_valid():
            # print(form.cleaned_data)
            task = form.save(commit=False)
            task.user = user
            task.save()
            return redirect('show_task')       
        else:
            return render(request, 'tasks/add_task.html', {'form':form})
    else:
        return redirect('login')


@login_required
def show_task(request):
    if request.user.is_authenticated:
        user = request.user
        cur_date = datetime.now()
        # print(cur_date)
        # task = TaskModel.objects.all()
        task =  TaskModel.objects.filter(user = user).order_by('-priority') 
        # task =  TaskModel.objects.filter(user = user).order_by('category') 
        # task =  TaskModel.objects.filter(user = user).order_by('due_date') 
        return render(request, 'tasks/show_task.html',{'task':task , 'cur_date':cur_date})
    else:
        return redirect('login')

def completed_task(request):
    if request.user.is_authenticated:        
        return render(request, 'tasks/completed_task.html')
    else:
        return redirect('added_task')


def edit_task(request, id):
    task = TaskModel.objects.get(pk = id)
    form = TaskForm(instance = task)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance = task )        
        if form.is_valid():
           form.save()                 
           return redirect('show_task')        
    return render(request, 'tasks/add_task.html', {'form':form})

def delete_task(request, id):
    task = TaskModel.objects.get(pk = id).delete()          
    return redirect('show_task')


def complete_status(request, id):
    task = TaskModel.objects.get(pk=id)
    task.status = 'Complete'
    task.save()
    return redirect('show_task')


@login_required
def completed_list(request):
    task = TaskModel.objects.filter(status='Complete')  
    # print(task)    
    return render(request, 'tasks/completed_task.html', {'task':task})



# filtering by category
def medium_ca(request):  
    task = TaskModel.objects.filter(category='Medium')    
    # task3 = TaskModel.objects.filter(category='Low')    
    return render(request, 'tasks/medium.html', {'task':task, })

def high_cat(request):  
    task = TaskModel.objects.filter(category='Heigh')    
    # task3 = TaskModel.objects.filter(category='Low')    
    return render(request, 'tasks/high.html', {'task':task, })

def low_cat(request):  
    task = TaskModel.objects.filter(category='Low')    
    # task3 = TaskModel.objects.filter(category='Low')    
    return render(request, 'tasks/low.html', {'task':task, })





