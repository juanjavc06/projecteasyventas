from django.shortcuts import render
from django.views import generic
from django.db.models import Q
from django.core import serializers

from django.http import JsonResponse, HttpResponse


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
			form = FormCategoria_Productos()
		
	queryset = Categoria_Productos.objects.all()
	context = {	'form':form	,'lista':queryset}
	
	return render(request,"dashboard/form_categoria_productos.html", context)

#-------------------PRODUCTOS------

def form_productos_view(request):
	form = FormProductos(request.POST)
	if form.is_valid():
		form.save()
		form = FormProductos()

	context = {	'form':form	}
	return render(request,"dashboard/form_productos.html", context)


def productos_buscar(request):
	queryset = Productos.objects.all()
	datos = []
	if request.method == 'GET':
		filtro = request.GET.get('filtro')
		if filtro is not None:
			print(filtro)
			data =  Productos.objects.filter(Q(nombre__icontains = filtro) | Q(descripcion__icontains = filtro))
			for dt in data:
				datos.append({"nombre": str(dt.nombre), 'descripcion': str(dt.descripcion), 'precio':str(dt.precio), 'id':int(dt.id)})
		else:
			return render(request, 'dashboard/form_productos_buscar.html',{'form': queryset})

	return HttpResponse(str(datos))


def get_products_by_id(request):
	queryset = Productos.objects.all()
	datos = []
	if request.method == 'GET':
		id_ = request.GET.get('id')
		if id_ is not None:
			data =  Productos.objects.filter(Q(id__icontains = id_))
			for dt in data:
				datos.append({"id": str(dt.id),"nombre": str(dt.nombre), 'descripcion': str(dt.descripcion), 'precio':str(dt.precio), 'id':int(dt.id)})
		else:
			HttpResponse("SETDATA")
	return HttpResponse(str(datos))

class form_productos_editar(generic.UpdateView):
    template_name = 'dashboard/form_productos_editar.html'
    model = Productos
    fields = '__all__'
    success_url = '../../../productos/buscar/'
		
#-----------------PROVEEDORES---------------
def form_proveedores_view(request):
	form = FormProveedores_Clientes(request.POST)
	if form.is_valid():
		form.save()
		form = FormProveedores_Clientes()

	context = {	'form':form	}
	return render(request,"dashboard/form_proveedores_clientes.html", context)

def proveedores_buscar(request):
	queryset = Proveedores_Clientes.objects.all()
	datos = []
	if request.method == 'GET':
		filtro = request.GET.get('filtro')
		if filtro is not None:
			print(filtro)
			data =  Proveedores_Clientes.objects.filter(Q(rfc__icontains = filtro) | Q(nombre_comercial__icontains = filtro))
			for dt in data:
				datos.append({"rfc": str(dt.rfc), 'nombre_comercial': str(dt.nombre_comercial), 'tipo': str(dt.tipo),'id':int(dt.id)})
		else:
			return render(request, 'dashboard/form_proveedores.html',{'form': queryset})

	return HttpResponse(str(datos))


class form_proveedores_editar(generic.UpdateView):
    template_name = 'dashboard/form_proveedor_editar.html'
    model = Proveedores_Clientes
    fields = '__all__'
    success_url = '../../../proveedores/'

#------------RELACION PRODUCTOS PROVEEDORES




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