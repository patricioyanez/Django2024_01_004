from django.db import models
# PASOS:
# 1.- definir los modelos
# 2.- preparar la migración
# py manage.py makemigrations alumnos
# 3.- ejecutar la migración (traspaso a la base de datos)
# py manage.py migrate
# 4.- bajar extension: sqlLite3 editor o similar y
# revisar la documentación para ver otros tipos de datos para agregar a models
# 5. continuar con el admin.py
# Create your models here.
# Create your models here.
class Escuela(models.Model):
    nombre      = models.CharField(max_length=100)
    activo      = models.IntegerField()

    def __str__(self):
        return self.nombre

class Carrera(models.Model):
    escuela     = models.ForeignKey('Escuela', on_delete=models.CASCADE)
    nombre      = models.CharField(max_length=100)
    version     = models.IntegerField()
    activo      = models.IntegerField()

    def __str__(self):
        return self.escuela.nombre + " " + self.nombre

class Alumno(models.Model):
    carrera     = models.ForeignKey('Carrera', on_delete=models.CASCADE)
    rut         = models.IntegerField()
    dv          = models.CharField(max_length=1)
    nombre      = models.CharField(max_length=50)
    apellido1   = models.CharField(max_length=50)
    apellido2   = models.CharField(max_length=50)
    nacimiento  = models.DateField()
    email       = models.CharField(max_length=100)
    direccion   = models.CharField(max_length=100)
    activo      = models.IntegerField()
# crear el str -> rut y nombre completo
    def __str__(self):
        return str(self.rut) + "-" + self.dv + "  " + self.nombre + " " + self.apellido1 + " " + self.apellido2
