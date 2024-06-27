from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="index"),
    path('sellerlogin/',views.sellersignup,name="sellersignup"),
    path('seller/',views.sellerlogin,name="sellerlogin"),
    path('sellerindex/',views.sellerindex,name="sellerindex"),
    path('logout/',views.logoutseller,name="logout"),
    path('additem/',views.additem,name="additem"),
    path('user/',views.userlogin,name="userlogin"),
    path('sellerindex/',views.usersignup,name="usersignup"),
    path('sellerproducts/',views.sellerproducts,name="sellerproduct"),
]