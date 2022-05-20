from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User
from .models import *
def home(request):
        if request.user.is_authenticated:
                stu=Students.objects.get(name=request.user.username)
                return render(request,'home.html',{'stu':stu})
        if request.method == "POST":
            print("YES")
            username=request.POST['Username']
            password=request.POST['Password']
            print(username+" "+password)
            user = authenticate(request, username=username, password=password)
            if user is not None:
               login(request, user)
               stu=Students.objects.get(name=user.username)
               print("NAME")
               print(stu.name)
               print("PENDING FEE")
               print(stu.pending_fee)
               return render(request,'home.html',{'stu':stu})
        else:
            print("NO")
        
        
        return render(request,'home.html')
def pay(request):
        if request.method == "POST":
                stu=Students.objects.get(name=request.user.username)
                stu.pending_fee=0;
                stu.save();
                return render(request,'completed.html')
        return render(request,'pay.html')

def completed(request):
        return render(request,'completed.html')
