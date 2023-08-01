from django.urls import path
from . import views

#importar auth_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('registro/', views.registro_usuario, name='usuario-registro'),
    path('login/', auth_views.LoginView.as_view(template_name='usuarios/login.html'), name='usuario-login'),
    path('perfil/', auth_views.LoginView.as_view(template_name='usuarios/perfil.html'), name='usuario-perfil')
]