from django import forms
# importar Model de models.py
from .models import Proveedor

# form no asociado, en este caso es para guardar informacion
# del formulario de contactos.
class ContactoForm(forms.Form):
    nombre = forms.CharField(label='Nombre')
    email = forms.EmailField(label='Correo electrónico')
    mensaje =  forms.CharField(widget=forms.Textarea)

class ProveedorForm(forms.ModelForm):
    nombre = forms.CharField(required=True)

    class Meta:
        model = Proveedor
        fields = ['nombre', 'email', 'mensaje']


