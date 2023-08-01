from django.contrib import admin
#importar Perfil
from .models import Perfil
# registrar Model para visualizar en la página de admin.
admin.site.register(Perfil)