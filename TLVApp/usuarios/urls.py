from django.urls import path
from . import views

#importar auth_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('registro/', views.registro_usuario, name='usuario-registro'),
    path('login/', views.custom_login, name='usuario-login'),
    path('logout/', views.custom_logout, name='usuario-logout'),
    path('perfil/', views.perfil, name='usuario-perfil')
]