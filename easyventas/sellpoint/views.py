from django.shortcuts import render


from  .models import *
from .forms import *

# Create your views here.

def index(request):
	return render(request, "dashboard/dashboard.html")

def login(request):
	return render(request, "dashboard/login.html")

def startSellPoint(request):
	return render(request, "dashboard/sellpoint.html")

def form_categorias_view(request):
	form = FormCategoria_Productos(request.POST)
	if request.method == 'POST':
		if form.is_valid():
			form.save()
		
	queryset = Categoria_Productos.objects.all()
	context = {	'form':form	,'lista':queryset}
	
	return render(request,"dashboard/form_categoria_productos.html", context)

def form_productos_view(request):
	form = FormProductos(request.POST)
	context = {	'form':form	}
	return render(request,"dashboard/form_productos.html", context)

#-------------------------Seccion Jenny -------------------------------------------

#USUARIOS 
def usuario(request):
	form = FormUsuarios(request.POST)
	return render(request,"dashboard/form_usuarios.html",{'form': form})

#Actualizar Usuario
def actualizar_usuario(request, id=1):
	form = FormUsuarios(request.POST)
	return render(request,"dashboard/actualizar_usuario.html",{'form': form})


#PERFILES
def perfiles(request):
	form = FormPerfiles(request.POST)
	return render(request,"dashboard/perfiles.html",{'form': form})


#ZONA
def zona(request):
	form = FormZona(request.POST)
	return render(request,"dashboard/form_zona.html",{'form': form})

#CORTE
def crear_corte(request):
	form = FormCortes(request.POST)
	return render(request,"dashboard/corte.html",{'form': form})

#INVENTARIO
def inventario(request):
	form = FormInventario(request.POST)
	return render(request,"dashboard/inventario.html",{'form':form})

#ALMACEN
def almacen(request):
	form = FormAlmacen(request.POST)
	return render(request,"dashboard/almacen.html",{'form': form})