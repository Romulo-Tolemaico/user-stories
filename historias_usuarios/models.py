# Create your models here.
from django.db import models

# Create your models here.
class Usuario(models.Model):
    cod_usu = models.IntegerField(primary_key=True,null=False,auto_created=True)
    nombre_usu = models.CharField(null=False,max_length=20)
    apellido_usu = models.CharField(null=False,max_length=20)
    correo_usu = models.CharField(null=False,max_length=25)
    clave_usu = models.CharField(null=False,max_length=20)

class Proyecto(models.Model):
    cod_pro = models.IntegerField(primary_key=True,null=False,auto_created=True)
    nombre_pro = models.CharField(null=False,max_length=20)
    descripcion_pro = models.CharField(null=False,max_length=200)
    cantidad_pro = models.IntegerField(default=0,null=False)
    usuario_pro = models.ForeignKey(Usuario, on_delete = models.CASCADE,null=False)

class Historia_Usuario(models.Model):
    cod_his_usu = models.IntegerField(primary_key=True,null=False,auto_created=True)
    titulo_his_usu = models.CharField(null=False,max_length=20)
    proyecto_his_usu = models.ForeignKey(Proyecto, on_delete = models.CASCADE,null=False)

class Version(models.Model):
    cod_ver = models.IntegerField(primary_key=True,null=False,auto_created=True)
    historia_ver = models.CharField(null=False,max_length=500)
    nro_ver = models.IntegerField(null=False,auto_created=True)
    historia_usuario_ver = models.ForeignKey(Historia_Usuario, on_delete = models.CASCADE,null=False)
