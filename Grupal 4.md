# Grupal 4 
# admin: tlv_admin
# password: telovendo

### Identifiquen claramente las diferencias entre los métodos GET y POST.

1. **GET**: Cuando usas GET, los datos viajan en la URL de la página web. Puedes ver los datos en la barra de direcciones y son útiles para obtener información del servidor, como abrir una página o mostrar resultados de búsqueda. Sin embargo, no es seguro para enviar información confidencial porque cualquiera puede verla.
2. **POST**: Con POST, los datos se envían de manera más segura y no se ven en la URL. Es perfecto para enviar información privada, como contraseñas o formularios grandes. También es útil cuando necesitas enviar mucha información, ya que no hay límite en la cantidad de datos que puedes enviar.

En resumen, utiliza GET para obtener información y mostrar cosas, y usa POST para enviar datos privados o grandes cantidades de información. Es importante elegir el método adecuado según lo que necesitas hacer en tu aplicación web.

### Guía para sintetizar los pasos necesarios para levantar un formulario desde Django con Forms y Models.

Paso 1: Configurar el proyecto Django

- Ejecuta el siguiente comando para crear un proyecto Django: `django-admin startproject myproject`.
- Ingresa al directorio del proyecto creado: `cd myproject`.

Paso 2: Crear una aplicación

- Crea una nueva aplicación dentro del proyecto con el siguiente comando: `python manage.py startapp myapp`.

Paso 3: Definir el modelo del formulario
En el archivo `models.py` de la aplicación, definimos el modelo utilizando `models.Model`. Supongamos que queremos un formulario de contacto con nombre, correo electrónico y mensaje:

```python
# myapp/models.py
from django.db import models

class Contacto(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.EmailField()
    mensaje = models.TextField()

    def __str__(self):
        return self.nombre

```

Paso 4: Crear el formulario
En el archivo `forms.py` de la aplicación, creamos el formulario utilizando `forms.Form` o `forms.ModelForm`. Usaremos `forms.ModelForm` para aprovechar el modelo definido anteriormente:

```python
# myapp/forms.py
from django import forms
from .models import Contacto

class ContactoForm(forms.ModelForm):
    class Meta:
        model = Contacto
        fields = ['nombre', 'correo', 'mensaje']

```

Paso 5: Agregar validaciones (opcional)
Si deseas agregar validaciones adicionales, puedes hacerlo en el formulario (`forms.py`) utilizando los métodos `clean_*`. Por ejemplo:

```python
# myapp/forms.py
from django import forms
from .models import Contacto

class ContactoForm(forms.ModelForm):
    class Meta:
        model = Contacto
        fields = ['nombre', 'correo', 'mensaje']

    def clean_nombre(self):
        nombre = self.cleaned_data['nombre']
        if len(nombre) < 3:
            raise forms.ValidationError('El nombre debe contener al menos 3 caracteres.')
        return nombre

    def clean_correo(self):
        correo = self.cleaned_data['correo']
        if not correo.endswith('@ejemplo.com'):
            raise forms.ValidationError('Por favor, utiliza un correo válido de ejemplo.com.')
        return correo

    def clean_mensaje(self):
        mensaje = self.cleaned_data['mensaje']
        if len(mensaje) < 10:
            raise forms.ValidationError('El mensaje debe tener al menos 10 caracteres.')
        return mensaje

```

Paso 6: Crear la vista
En el archivo `views.py` de la aplicación, creamos una vista que procese el formulario y muestre la página de contacto:

```python
# myapp/views.py
from django.shortcuts import render
from .forms import ContactoForm

def contacto(request):
    if request.method == 'POST':
        form = ContactoForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'contacto_exitoso.html')  # Redirigir a una página de éxito
    else:
        form = ContactoForm()
    return render(request, 'contacto.html', {'form': form})

```

Paso 7: Configurar URL
En el archivo `urls.py` de la aplicación, agregamos una URL para la vista creada en el paso anterior:

```python
# myapp/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('contacto/', views.contacto, name='contacto'),
]

```

Paso 8: Crear la plantilla
Crea un archivo de plantilla (por ejemplo, `contacto.html`) en la carpeta `templates/myapp/` para mostrar el formulario:

```html
<!-- myapp/templates/myapp/contacto.html -->
<!DOCTYPE html>
<html>
<head>
    <title>Contacto</title>
</head>
<body>
    <h1>Contacto</h1>
    <form method="post">
        {% csrf_token %}
        {{ form.as_p }}
        <button type="submit">Enviar</button>
    </form>
</body>
</html>

```

Paso 9: Actualizar la configuración del proyecto
Agrega la aplicación a la configuración del proyecto en el archivo `settings.py`:

```python
# myproject/settings.py
INSTALLED_APPS = [
    ...
    'myapp',
    ...
]

```

Paso 10: Ejecutar el servidor
Inicia el servidor Django con el comando: `python manage.py runserver`.