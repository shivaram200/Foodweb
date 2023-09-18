from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name='home'),
    path('services',views.services,name='services'),
    path('aboutus',views.aboutus,name='aboutus'),
    path('contactus',views.contactus,name='contactus'),
    path('login',views.login,name='login'),
    path('signup',views.signup,name='signup'),
    path('orders',views.orders,name='orders'),
    path('logout',views.logout,name='logout')
]