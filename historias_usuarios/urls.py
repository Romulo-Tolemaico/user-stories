from django.urls import path
from . import views

urlpatterns = [
    #path('about/',views.about)
    #path('login/',views.verificarUsuario),
    path('',views.loging),
    path('login',views.loging),
    path('register-user',views.register),
    path('about',views.about),
    path('registrar',views.registrar),
    path('iniciar',views.iniciarSesion)
]