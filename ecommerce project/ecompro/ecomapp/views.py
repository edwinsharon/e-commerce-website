from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    return render(request,"index.html")
def sellersignup(request):
    if request.POST:
        email=request.POST.get('email')
        username=request.POST.get('username')
        password=request.POST.get('password')
        confirmpassword=request.POST.get('confirmpassword')
        if confirmpassword == password:
            User.objects.create_user(username=username,password=password,email=email)
            return redirect('sellerlogin')
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
    return render (request,"addpro.html")
