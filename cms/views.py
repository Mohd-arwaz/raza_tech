from django.shortcuts import render
from django.http import HttpResponse
from .models import Employes
# Create your views here.

def home(request):
    return render(request, "index.html") 

def team(request):
    return render(request, "team.html")   

def services(request):
    return render(request, "services.html")    

def contact(request):
    return render(request, "contact.html" )   


