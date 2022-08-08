from django.contrib import admin
from django.urls import path
from .views.home import store,Index,htl1,htl2,htl3,htl4,htl5,lth1,lth2,lth3,lth4,lth5,alogin,users
from .views.CovidEssentials import Index1 , CovidEssentials
from .views.healthCproducts import Index2 , healthCproducts
from .views.personalcare import Index3 , personalcare
from .views.MensGrooming import Index4 , MensGrooming
from .views.makeup import Index5 , makeup
from .views.signup import Signup
from .views.login import Login , logout
from .views.cart import Cart
from .views.checkout import CheckOut
from .views.orders import OrderView
from .middlewares.auth import  auth_middleware
from django.views.generic.base import TemplateView


urlpatterns = [
    
    path('', Index.as_view(), name='homepage'),
    path('Index1', Index1.as_view(), name='Index1'),
    path('Index2', Index2.as_view(), name='Index2'),
    path('Index3', Index3.as_view(), name='Index3'),
    path('Index4', Index4.as_view(), name='Index4'),
    path('Index5', Index5.as_view(), name='Index5'),
    
    path('alogin',alogin.as_view(), name='alogin'),
    path('users',users, name='users'),

    path('htl1',htl1, name='htl1'),
    path('htl2',htl2, name='htl2'),
    path('htl3',htl3, name='htl3'),
    path('htl4',htl4, name='htl4'),
    path('htl5',htl5, name='htl5'),

    path('lth1',lth1, name='lth1'),
    path('lth2',lth2, name='lth2'),
    path('lth3',lth3, name='lth3'),
    path('lth4',lth4, name='lth4'),
    path('lth5',lth5, name='lth5'),


    path('store', store , name='store'),
    path('CovidEssentials', CovidEssentials , name='CovidEssentials'),
    path('healthCproducts', healthCproducts , name='healthCproducts'),
    path('personalcare', personalcare , name='personalcare'),
    path('MensGrooming', MensGrooming , name='MensGrooming'),
    path('makeup', makeup , name='makeup'),
    path('signup', Signup.as_view(), name='signup'),
    path('login', Login.as_view(), name='login'),
    path('logout', logout , name='logout'),
    path('cartt', auth_middleware(Cart.as_view()) , name='cart'),
    path('check-out', CheckOut.as_view() , name='checkout'),
    path('orders', auth_middleware(OrderView.as_view()), name='orders'),

    
    path("aboutus",TemplateView.as_view(template_name="aboutus.html"),name="AboutUsPage"),
    path("contactus",TemplateView.as_view(template_name="contactus.html"),name="ContactUsPage"),
    #path("healthCproducts",TemplateView.as_view(template_name="healthCproducts.html"),name="healthCproducts"),
    #path("personalcare",TemplateView.as_view(template_name="personalcare.html"),name="personalcare"),
    #path("MensGrooming",TemplateView.as_view(template_name="MensGrooming.html"),name="MensGrooming"),
    #path("makeup",TemplateView.as_view(template_name="makeup.html"),name="makeup"),
    path("healthlibrary",TemplateView.as_view(template_name="healthlibrary.html"),name="healthlibrary"),
    path("medicine",TemplateView.as_view(template_name="medicine.html"),name="medicine"),

]

