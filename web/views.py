from django.shortcuts import render
from .models import Producto
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView

def home(request):
    productos = Producto.objects.all().filter(premium=False)
    return render(request, 'web/home.html', {'productos': productos})

@login_required
def premium(request):
    productos = Producto.objects.filter(premium=True)
    return render(request, 'web/premium.html', {'productos': productos})

class ProductoDetalle(DetailView):
    model = Producto
    template_name = 'web/detalle.html'
    context_object_name = 'producto'