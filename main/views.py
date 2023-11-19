from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def index(request):
    return render(request, 'main/index.html', {})


def Cus2_LoginPage(request):
    return render(request, 'main/Cus2_LoginPage.html', {})


def Cus3_RegisterPage(request):
    return render(request, "main/Cus3_RegisterPage.html", {})


def Admin1_LoginPage(request):
    return render(request, "main/Admin1_LoginPage.html", {})

def Admin2_HomePage(request):
    return render(request, "main/Admin2_HomePage.html", {})

def Admin3_AddTrainPage(request):
    return render(request, "main/Admin3_AddTrainPage.html", {})
def Admin5_AboutUs(request):
    return render(request, "main/Admin5_AboutUs.html", {})


