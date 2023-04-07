from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.

def loging(request):
    return render(request,'log.html')

def about(request):
    title = ':)'
    return render(request,'about.html',{ 'title' : title})

def verificarUsuario(request):
    usuarios = request.POST['']
    clave = request.POST['']
    #cuenta = Usuario.objects.create()
    return render(request,'login.html',{'usuarios':usuarios}) #usuarios [{},{},{}]

def layout(request):
    return render(request,'layout.html')