from django.shortcuts import render, redirect
from .forms import RegistrationForm, updateForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate




def register(request):
    form = RegistrationForm()
    if request.method =='POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Account Created Succesfully')
            form.save()
            # print(form.cleaned_data)                      
            return redirect('add_task')
    else:
        form = RegistrationForm()              
    return render(request, 'accounts/register.html',{'form':form})


def user_login(request):
    form = AuthenticationForm() 
    if request.method =='POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            name = form.cleaned_data['username']
            userpass = form.cleaned_data['password']
            user = authenticate(username=name, password=userpass)
            if user is not None:
                login(request,user)            
                return redirect('show_task')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html',{'form':form} )

def user_logout(request):
    logout(request)
    return redirect('login')


def profile(request):   
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = updateForm(request.POST, instance = request.user)
            if form.is_valid():
                messages.success(request, 'Account Updated Succesfully')
                form.save()
                return redirect('show_task')
        else:
            form = updateForm(instance = request.user)
        return render(request, 'accounts/profile.html',{'form':form})
            
    else:
        return redirect('register')
        
    