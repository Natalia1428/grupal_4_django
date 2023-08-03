from django.urls import path
from . import views

urlpatterns = [
    path('', views.vista_1, name='home'),
    path('cliente/', views.vista_2, name='cliente'),
    path('contacto/', views.vista_3, name='contacto'),
    # path('cliente/<int:pk>', views.DetailView.as_view(), name='cliente-detail'),
    path('cliente/new', views.CreateUsuarioView.as_view(), name='cliente-create'),
    path('cliente/<int:pk>/update', views.UpdateUsuarioView.as_view(), name='cliente-update') 

]