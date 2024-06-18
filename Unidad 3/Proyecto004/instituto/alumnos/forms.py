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
            }),
            'nombre' : forms.TextInput(attrs={
                'class' : 'form-control',
                'placeholder': 'Ingrese su nombre'
            }),
            'apellido1' : forms.TextInput(attrs={
                'class' : 'form-control',
                'placeholder': 'Ingrese su 1er apellido'
            }),
            'apellido2' : forms.TextInput(attrs={
                'class' : 'form-control',
                'placeholder': 'Ingrese su 2do apellido'
            }),
            'foto' : forms.ClearableFileInput(attrs={
                'class': 'form-control'
            }),
            'activo' : forms.CheckboxInput(attrs={
                'class' : 'form-check-input', 
                'value' : '1'
            })
        }

