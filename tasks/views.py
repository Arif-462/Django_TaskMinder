from django.shortcuts import render,redirect
from .models import TaskModel
from .forms import TaskForm
from django.contrib.auth.decorators import login_required
from django.utils.timezone import datetime




# Create your views here.

# user can add his/jer task
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


# user can thier total task
@login_required
def show_task(request):
    if request.user.is_authenticated:
        user = request.user
        cur_date = datetime.now()
        # print(cur_date)
        task =  TaskModel.objects.filter(user = user).order_by('-priority') 
        return render(request, 'tasks/show_task.html',{'task':task , 'cur_date':cur_date})
    else:
        return redirect('login')
    
    

# user can see thier complete task
def completed_task(request):
    if request.user.is_authenticated: 
        user = request.user       
        return render(request, 'tasks/completed_task.html')
    else:
        return redirect('added_task')


# user can edit or update thier task
def edit_task(request, id):
    task = TaskModel.objects.get(pk = id)
    form = TaskForm(instance = task)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance = task )        
        if form.is_valid():
           form.save()                 
           return redirect('show_task')        
    return render(request, 'tasks/add_task.html', {'form':form})


# user can delete thier task
def delete_task(request, id):
    if request.user.is_authenticated:
        task = TaskModel.objects.get(pk = id).delete()          
        return redirect('show_task')
    else:
        return redirect('added_task')

# user can do complete option thier task
def complete_status(request, id):
    if request.user.is_authenticated:
        task = TaskModel.objects.get(pk=id)
        task.status = 'Complete'
        task.save()
        return redirect('show_task')
    else:
        return redirect('added_task')

# user can see their total completed task
def completed_list(request):
    if request.user.is_authenticated:
        task = TaskModel.objects.filter(user = request.user, status='Complete')  
        # print(task)    
        return render(request, 'tasks/completed_task.html', {'task':task})
    else:
        return redirect('login')



# filtering by category
def medium_cat(request):  
    if request.user.is_authenticated:
        task = TaskModel.objects.filter(user=request.user, category='Medium')      
        return render(request, 'tasks/medium.html', {'task':task, })
    else:
        return redirect('home')
    
# filtering by high category
def high_cat(request):  
    if request.user.is_authenticated:
        task = TaskModel.objects.filter(user = request.user, category='Heigh')        
        return render(request, 'tasks/high.html', {'task':task, })
    else:
        return redirect('home')

# filtering by low category
def low_cat(request): 
    if request.user.is_authenticated:
        task = TaskModel.objects.filter(user=request.user, category='Low')      
        return render(request, 'tasks/low.html', {'task':task, })
    else:
        return redirect('home')





