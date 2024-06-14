from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib import messages
from .models import *

# Create your views here.
def index(request):
    return render(request,"index.html")
def sellersignup(request):
    if request.POST:
        email=request.POST.get('email')
        username=request.POST.get('username')
        password=request.POST.get('password')
        confirmpassword=request.POST.get('confirmpassword')
        
        if not username or not email or not password or not confirmpassword:
            messages.error(request,'all fields are required.')

        elif confirmpassword != password:
            messages.error(request,"password doesnot match")
           
        elif User.objects.filter(email=email).exists():
            messages.error(request,"email already exist")
           
        elif User.objects.filter(username=username).exists():
            messages.error(request,"username already exist")

        else:
           
            user = User.objects.create_user(username=username, email=email, password=password)    
            user.is_staff=True
            user.save()
            messages.success(request,"account created successfully")
            return render(request, "sellercreate.html")
    return render(request,"sellercreate.html")    
           

def sellerlogin(request):
    if 'username' in request.session:
        return redirect('sellerindex')
    if request.POST:
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            request.session['username']=username
            return redirect("sellerindex")
    return render(request,"sellerlogin.html")    
def sellerindex(request):
    return render(request,"sellerindex.html")    
def logoutseller(request):
    logout(request)
    return redirect('sellerlogin')
def additem(request):
    if request.POST:
        
        productname=request.POST.get("productname")
        prize=request.POST.get("prize")
        offer=request.POST.get("offer")
        speed=request.POST.get("speed")
        color=request.POST.get("color")
        description=request.POST.get("description")
        category=request.POST.get("category")
        image=request.POST.get("image")
        if not productname or not prize or not offer or not speed or not color or not description or not category or not image:
            messages.error(request,"all fields are required")

        else:
            probj=product(productname=productname,prize=prize,offer=offer,speed=speed,color=color,description=description,category=category,image=image)
            probj.save()
            messages.success(request,"product added")    
            return redirect("additem")
        

    return render (request,"addpro.html")

