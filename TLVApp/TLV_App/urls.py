from django.urls import path
from . import views

urlpatterns = [
    path('', views.vista_1, name='home'),
    path('cliente/', views.vista_2, name='cliente'),
    path('contacto/', views.vista_3, name='contacto')
]