from django.shortcuts import redirect, render
from .models import Usuario
from .forms import ProveedorForm

#importar messages
from django.contrib import messages

# vistas genéricas Django
from django.views.generic import CreateView, DetailView, UpdateView

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

# detalles de los clientes
class DetailUsuarioView(DetailView):
    model = Usuario


# crear un usuario
class CreateUsuarioView(CreateView):
    model = Usuario
    template_name = 'create_cliente.html'
    fields = ['nombre', 'apellido', 'pais', 'edad', 'hobby']

    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)
    
class UpdateUsuarioView(UpdateView):
    model = Usuario
    template_name = 'cliente_update.html'
    fields = ['pais', 'edad', 'hobby']
    

    def form_valid(self,form):
        nombre=form.instance.nombre
        apellido=form.instance.apellido 
        form.instance.autor = self.request.user
        response = super().form_valid(form)
        messages.success(self.request, f'Cliente {nombre} {apellido} actualizado exitosamente!')
        return response
