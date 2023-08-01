from django.contrib import admin
from .models import Usuario, Proveedor


@admin.register(Usuario)
class RequestDemoAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Usuario._meta.get_fields()]


admin.site.register(Proveedor)