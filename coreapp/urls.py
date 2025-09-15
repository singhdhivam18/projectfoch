from django.contrib import admin
from django.urls import path
from coreapp import views

urlpatterns = [
    
    #path('',views.index,name='home'),
    #path('about',views.about,name='about'),
    #path('register',views.register,name='register'),
    path('dashboard',views.dashboard,name="dashboard")
    #path('insert',views.insert,name="insert")
]