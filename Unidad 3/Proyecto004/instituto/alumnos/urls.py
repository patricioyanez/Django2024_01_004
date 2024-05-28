from django.urls import path
from . import views

#http://127.0.0.1:8000/alumnos/index
urlpatterns = [
    path('index', views.index , name='index'),
    path('listarAlumnos', views.listarAlumnos , name='listarAlumnos'),
]