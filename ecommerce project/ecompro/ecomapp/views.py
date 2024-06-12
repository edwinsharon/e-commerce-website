from django.shortcuts import render
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    return render(request,"index.html")
def sellersignup(request):
    if request.POST:
        username=request.POST.get('username')
        password=request.POST.get('password')
        User.objects.create_user(username=username,password=password)
        return redirect('sellerlogin')
    return render(request,"sellerlogin.html")

def 