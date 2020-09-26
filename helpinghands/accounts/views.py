from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import CustomUserForm
from django.contrib import messages
from django.contrib.auth.forms import authenticate

def register(request):
    form = CustomUserForm()

    if request.method == 'POST':
        form = CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('first_name')
            messages.success(request, 'Welcome '+ user)
            return redirect('accounts-login')

    return render(request, 'accounts/register.html', {'form':form})

def about(request):
    return render(request, 'accounts/about.html')

def login(request):
    return render(request, 'accounts/login.html')