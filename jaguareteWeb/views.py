from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
#def index(request):
#    return HttpResponse("<h1 style=\"color:blue;font-family:Monospace\"> Holiwis</h1>")

def index(request):
    return render(request, "signin.html")