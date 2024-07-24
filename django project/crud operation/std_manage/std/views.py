from django.shortcuts import render,redirect
from . import models

from .models import student

# Create your views here.

def home(request):
    std=student.objects.all()
    return render(request,"std/home.html",{'std':std})


def std_add(request):
    if request.method=='POST':
        print("Added")
        #retrive the useer inputs
        stds_roll=request.POST.get("std_roll")
        stds_name=request.POST.get("std_name")
        stds_email=request.POST.get("std_email")
        stds_address=request.POST.get("std_address")
        stds_phone=request.POST.get("std_phone")
        
        #create an object for models
        s=student()
        s.roll=stds_roll
        s.name=stds_name
        s.email=stds_email
        s.address=stds_address
        s.phone=stds_phone
        
        s.save()
        return redirect('/std/home/')          
    
    return render(request,"std/add_std.html", {})


def delete_std(request,roll):
    s=student.objects.get(pk=roll)
    s.delete()
    
    return redirect('/std/home')

def update_std(request,roll):
        std=student.objects.get(pk=roll)    
        return render(request,"std/update_std.html",{'std':std})
    
def

    
