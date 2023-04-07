from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.

def loging(request):
    return render(request,'log.html')

def register(request):
    return render(request,'Register.html')

def about(request):
    return render(request,'about.html')

def registrar(request):
    Usuario.objects.create(
        cod_usu = Usuario.objects.count()+1,
        nombre_usu = request.POST['nombre'],
        apellido_usu = request.POST['apellido'],
        correo_usu = request.POST['email'],
        clave_usu = request.POST['password']
    )
    return render(request,'log.html')

def iniciarSesion(request):
    for id in Usuario.objects.all():
        if id.correo_usu == request.POST['email'] and id.clave_usu == request.POST['password']:
            print("encontrado")
            return render(request,'proyectos.html',{'proyectos':Proyecto.objects.all()})
    return render(request,'log.html')

