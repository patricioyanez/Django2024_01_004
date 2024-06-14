from django import forms
from django.forms import ModelForm


from .models import Usuario

class UsuarioForm(ModelForm):
    class Meta:
        model = Usuario
        fields="__all__"
        labels={
            'apellido1' : '1er Apellido',
            'apellido2' : '2do Apellido',
        }
        widgets={
            'email' : forms.TextInput(attrs={
                'class' : 'form-control',
                'placeholder': 'Ingrese su correo'
            })
        }

