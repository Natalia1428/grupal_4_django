from django.shortcuts import redirect, render
from .models import Usuario
from .forms import ProveedorForm

def vista_1(request):
    return render(request, 'landing.html')

def vista_2(request):
    contexto_clientes = {
        'clientes' : Usuario.objects.all(),
    }
    return render(request, 'cliente.html', contexto_clientes)

def vista_3(request):
    #validar tipo de request
    if request.method == "POST":
        # creamos un objeto de la clase Form.
        proveedor_post = ProveedorForm(request.POST)
        if proveedor_post.is_valid():
            proveedor = proveedor_post.save(commit=False)
            proveedor.save()
            #redireccionar nuevamente a contacto.html (limpiar formulario)
            return redirect('contacto')
    proveedor_formulario = ProveedorForm()
    return render(request, 'contacto.html', {'formulario':proveedor_formulario})
    