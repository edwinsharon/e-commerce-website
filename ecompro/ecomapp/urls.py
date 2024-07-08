from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
    path('',views.index,name="index"),
    path('contact/',views.contact,name="contact"),
    path('about/',views.about,name="about"),
    path('gallery/',views.gallery,name="gallery"),
    path('testimonial/',views.testimonial,name="testimonial"),
    path('sellerlogin/',views.sellersignup,name="sellersignup"),
    path('seller/',views.sellerlogin,name="sellerlogin"),
    path('sellerindex/',views.sellerindex,name="sellerindex"),
    path('logout/',views.logoutseller,name="logout"),
    path('additem/',views.additem,name="additem"),
    path('user/',views.userlogin,name="userlogin"),
    path('usersignup/',views.usersignup,name="usersignup"),
    path('sellerproducts/',views.sellerproducts,name="sellerproduct"),
    path('logoutuser/',views.logoutuser,name="logoutuser"),
    path('delete_g/<int:pk>',views.delete_g,name="delete_g"),
    path('edit_g/<int:pk>',views.edit_g,name="edit_g"),  
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)