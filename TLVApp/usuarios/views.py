
from django.shortcuts import render, redirect
#1) importar messages
from django.contrib import messages

#2) importar forms.py
from .forms import RegistrarUsuarioForm

#3) importar login required
from django.contrib.auth.decorators import login_required

# importar logout, login, authenticate
from django.contrib.auth import logout, login, authenticate

# importar AuthenticationForm
from django.contrib.auth.forms import AuthenticationForm

def registro_usuario(request):
    # usuarios logeados no pueden registrar una cuenta nueva.
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == "POST":
        form = RegistrarUsuarioForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data['username']
            login(request, user)
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

# *** IMPORTANTE implementar en settings.py LOGIN_REDIRECT_URL = "" ***
# @login_required
# def perfil(request):
#     if request.method == 'POST':
#         formulario_usuario = RegistrarUsuarioForm(request.POST, isinstance=request.user)

#         # validar formulario.
#         if formulario_usuario.is_valid():
#             usuario = formulario_usuario.save(commit=False)

#             username = formulario_usuario.cleaned_data['username']

#             formulario_usuario.save()

#     formulario = RegistrarUsuarioForm()

#     return render(request, 'usuarios/login.html', {'formulario':formulario})

@login_required
def custom_logout(request):
    logout(request)
    messages.info(request, 'Sesión finalizada correctamente!')
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