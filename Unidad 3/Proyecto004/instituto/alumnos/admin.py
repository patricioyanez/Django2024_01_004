from django.contrib import admin
from .models import Escuela, Carrera, Alumno

# 1.- ir a http://127.0.0.1:8000/admin
# 2.- crear un usuario para el admin en la consola
# ir a la carpeta del proyecto (donde esta manage.py)
# py manage.py createsuperuser
# omitir validacion de clave
# 3.- loguearse en la pagina
# 4.- agregar crud en admin.py

# Register your models here.
admin.site.register(Escuela)
admin.site.register(Carrera)
admin.site.register(Alumno)

# TAREAS:
# revisar la documentación para ver otros tipos de datos para agregar a models
# agregar crud para carrera y alumno
# agregar 5 filas para cada modelos