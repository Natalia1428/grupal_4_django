
from django.shortcuts import render, redirect
#1) importar messages
from django.contrib import messages

#2) importar forms.py
from .forms import RegistrarUsuarioForm, ActualizarUsuarioForm, ActualizarPerfilForm
#3) importar login required
from django.contrib.auth.decorators import login_required

# importar logout, login, authenticate
from django.contrib.auth import logout, login, authenticate, get_user_model

# importar AuthenticationForm
from django.contrib.auth.forms import AuthenticationForm

# importar models Groups de Django
from django.contrib.auth.models import Group

def registro_usuario(request):
    # usuarios logeados no pueden registrar una cuenta nueva.
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == "POST":
        form = RegistrarUsuarioForm(request.POST)
        if form.is_valid():
            user = form.save()
            tipo_usuario = form.cleaned_data['tipo_usuario']

            # asignaciones de tipo de usuario.
            if tipo_usuario == 'administrador':
                grupo = Group.objects.get(name='administrador')
            elif tipo_usuario == 'moderador':
                grupo = Group.objects.get(name='moderador')
            elif tipo_usuario == 'usuario_comun':
                grupo = Group.objects.get(name='usuario_comun')

            user.groups.add(grupo)
            form.save()

            # login(request, user)
            messages.success(request, f'Nueva cuenta creada: {user.username}')
            return redirect('home')
        else:
            for error in list(form.errors.values()):
                print(request, error)
    else:
        form = RegistrarUsuarioForm()
    
    return render(
        request = request,
        template_name="usuarios/registro.html",
        context={"form":form}
    )

# *** IMPORTANTE implementar en settings.py LOGIN_REDIRECT_URL = " " ***
@login_required
def perfil(request):
    if request.method == "POST":
        formulario_usuario = ActualizarUsuarioForm(request.POST, instance=request.user)
        formulario_perfil = ActualizarPerfilForm(request.POST, instance=request.user.perfil)
        if formulario_usuario.is_valid() and formulario_perfil.is_valid():
            formulario_usuario.save()
            formulario_perfil.save()
            messages.success(request, 'Datos actualizados correctamente!')
            return redirect('usuario-perfil')
    else:
        formulario_usuario = ActualizarUsuarioForm(instance=request.user)
        formulario_perfil = ActualizarPerfilForm(instance=request.user.perfil)
    contexto = {
        'formulario_usuario':formulario_usuario,
        'formulario_perfil': formulario_perfil
    }
    return render(request, 'usuarios/perfil.html', contexto)    

@login_required
def custom_logout(request):
    logout(request)
    messages.info(request, f'Sesión finalizada correctamente!')
    return redirect('home')

def custom_login(request):
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == "POST":
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid(): # si el formulario de login es válido.
            user = authenticate(
                username = form.cleaned_data['username'],
                password = form.cleaned_data['password']
            )
            if user is not None:
                login(request, user)
                messages.success(request, f'Bienvenido {user.username}')
                return redirect('home')
        else:
            for error in list(form.errors.values()):
                messages.error(request, error)
    
    form = AuthenticationForm()

    return render(
        request=request,
        template_name='usuarios/login.html',
        context={'form':form}
    )