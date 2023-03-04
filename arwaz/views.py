from django.shortcuts import render
from django.http import HttpResponse
from .models import student

# Create your views here.
def home(request):
    student_page= student.objects.get(pk =1)
    data = {'Name':student_page.Name, 'City':student_page.city,'Age':student_page.age}
    return render(request, "arwaz.html", data)

def cont(request):
    return render(request, "cont.html")