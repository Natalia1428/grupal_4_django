from typing import Any
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from .models import Perfil

class RegistrarUsuarioForm(UserCreationForm):


    email = forms.EmailField(required=True, label='Correo electrónico')
    username = forms.CharField(required=True ,label='Nombre usuario')


    opciones = (
        ('administrador', 'administrador'),
        ('moderador', 'moderador'),
        ('usuario_comun', 'usuario_comun')
    )

    tipo_usuario = forms.ChoiceField(choices=opciones, widget=forms.Select(attrs={'class': 'form-select'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'tipo_usuario']


# actualizar datos del usuario
class ActualizarUsuarioForm(forms.ModelForm):
    first_name = forms.CharField(label="Nombre")
    last_name = forms.CharField(label="Apellido")
    email = forms.EmailField()

    class Meta:
        model = get_user_model()
        fields = ['first_name', 'last_name', 'email']

class ActualizarPerfilForm(forms.ModelForm):
    class Meta:
        model = Perfil()
        fields = ['pais']

