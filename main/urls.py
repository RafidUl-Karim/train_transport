from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('Cus2_LoginPage/', views.Cus2_LoginPage, name='Cus2_LoginPage'),
    path('Cus3_RegisterPage/', views.Cus3_RegisterPage, name='Cus3_RegisterPage'),
    path('Admin1_LoginPage/', views.Admin1_LoginPage, name='Admin1_LoginPage'),
    path('Admin2_HomePage/', views.Admin2_HomePage, name='Admin2_HomePage'),
    path('Admin3_AddTrainPage/', views.Admin3_AddTrainPage, name='Admin3_AddTrainPage'),
    path('Admin5_AboutUs/', views.Admin5_AboutUs, name='Admin5_AboutUs')

]