from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ProductForm
from django.contrib import messages

# Create your views here.

def home(request):
    return HttpResponse('<h1>Home</h1>' )

def home2(request):
    return render(request, 'accounts/base.html')

from django.contrib.auth.decorators import login_required

@login_required
def fillListForm(request):

    
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            form.user = request.user
            form.instance.admin =  request.user
            form.save()
            # username = form.changed_data.get("username")
            # messages.success(request, f'Listing Created')
            return redirect("home")
        else:
            print("add**************************************")
            print(form.errors)
            return redirect("home")

    else:
        form = ProductForm()
    return render(request, 'accounts/st_form.html', {"form" : form , "info" : "form check"})



