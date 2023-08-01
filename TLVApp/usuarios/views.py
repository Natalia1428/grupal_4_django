from django.shortcuts import render, redirect
#1) importar messages
from django.contrib import messages

#2) importar forms.py
from .forms import RegistrarUsuarioForm

#3) importar login required
from django.contrib.auth.decorators import login_required

def registro_usuario(request):
    if request.method == 'POST':
        formulario_post = RegistrarUsuarioForm(request.POST)
        #validar formulario
        if formulario_post.is_valid():
            usuario = formulario_post.save(commit=False)
            
            username = formulario_post.cleaned_data['username']

            # mensaje de éxito
            messages.success(request, f'Cuenta registrada exitosamente para el usuario {username}')

            # guardar formulario
            formulario_post.save()
            
            # redireccionar a la página de log in.
            return redirect('usuario-registro')
        else:
            messages.error(request, f'Hubo un error en el proceso de registro del usuario  {username}')

    formulario = RegistrarUsuarioForm()
    
    return render(request, 'usuarios/registro.html', {'formulario':formulario})

# *** IMPORTANTE implementar en settings.py LOGIN_REDIRECT_URL ***
@login_required
def perfil(request):
    if request.method == 'POST':
        formulario_usuario = RegistrarUsuarioForm(request.POST, isinstance=request.user)

        # validar formulario.
        if formulario_usuario.is_valid():
            usuario = formulario_usuario.save(commit=False)

            username = formulario_usuario.cleaned_data['username']

            formulario_usuario.save()

    formulario = RegistrarUsuarioForm()

    return render(request, 'usuarios/login.html', {'formulario':formulario})