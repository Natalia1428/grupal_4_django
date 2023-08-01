from typing import Any
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
#importar models.py (Perfil)
from .models import Perfil

class RegistrarUsuarioForm(UserCreationForm):
    email = forms.EmailField(required=True, label='Correo electrónico')
    username = forms.CharField(label='Nombre usuario')

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
