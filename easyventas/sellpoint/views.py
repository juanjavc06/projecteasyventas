from django.shortcuts import render
from django.views import generic
from django.db.models import Q
from django.core import serializers
from django.urls import reverse_lazy

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




#-------------------------Seccion Jenny -------------------------------------------

#USUARIOS 
#Funcion para dar de alta un usuario
def usuario(request):
	form = FormUsuarios(request.POST)
	if form.is_valid():
		form.save()
		form = FormUsuarios()

	return render(request,"dashboard/form_usuarios.html",{'form': form})

#Funcion para buscar un usuario
def usuarios_buscar(request):
	queryset = Usuarios.objects.all()
	datos = []
	if request.method == 'GET':
		filtro = request.GET.get('filtro')
		if filtro is not None:
			print(filtro)
			data =  Usuarios.objects.filter(Q(usuarios__icontains = filtro) | Q(perfil__icontains = filtro))
			for dt in data:
				datos.append({"usuarios": str(dt.usuarios), 'nombre': str(dt.nombre), 'password':str(dt.password),'perfil':str(dt.perfil)})
		else:
			return render(request, 'dashboard/form_usuarios_buscar.html',{'form': queryset})

	return HttpResponse(str(datos))	

#Actualizar Usuario
class usuarios_editar(generic.UpdateView):
	template_name   = 'dashboard/form_usuarios_editar.html'
	model           = Usuarios
	fields          = '__all__'
	success_url     = '../../../usuarios/buscar/'

#PERFILES
def perfiles(request):
	form = FormPerfiles(request.POST)
	if form.is_valid():
		form.save()
		form = FormPerfiles()
	return render(request,"dashboard/perfiles.html",{'form': form})


#ZONA
def zona(request):
	form = FormZona(request.POST)
	if form.is_valid():
		form.save()
		form = FormZona()

	return render(request,"dashboard/form_zona.html",{'form': form})

#Funcion para actualizar las zonas
class zona_editar(generic.UpdateView):
	template_name   = 'dashboard/form_zona_editar.html'
	model           = Zona
	fields          = '__all__'
	success_url     = '../../../zona/buscar/'

def zona_buscar(request):
	queryset = Zona.objects.all()
	datos = []
	if request.method == 'GET':
		filtro = request.GET.get('filtro')
		if filtro is not None:
			print(filtro)
			data =  Zona.objects.filter(Q(zona__icontains = filtro))
			for dt in data:
				datos.append({"zona": str(dt.zona), 'almacen': str(dt.almacen)})
		else:
			return render(request, 'dashboard/form_zona_buscar.html',{'form': queryset})

	return HttpResponse(str(datos))	

#CORTE
def crear_corte(request):
	form = FormCortes(request.POST)
	if form.is_valid():
		form.save()
		form = FormCortes()
	return render(request,"dashboard/corte.html",{'form': form})


#INVENTARIO
#Funcion para dar de alta inventario
def inventario(request):
	form = FormInventario(request.POST)
	if form.is_valid():
		form.save()
		form = FormInventario()

	return render(request,"dashboard/form_inventario.html",{'form':form})

#Funcion para buscar inventario por producto
def inventario_buscar(request):
	queryset = Inventario.objects.all()
	datos = []
	if request.method == 'GET':
		filtro = request.GET.get('filtro')
		if filtro is not None:
			print(filtro)
			data =  Inventario.objects.filter(Q(existencias__icontains = filtro) | Q(producto__icontains = filtro) | Q(zona__icontains = filtro))
			for dt in data:
				datos.append({"existencias": str(dt.existencias), 'producto': str(dt.producto), 'zona':str(dt.zona)})
		else:
			return render(request, 'dashboard/form_inventario_buscar.html',{'form': queryset})

	return HttpResponse(str(datos))	

#Funcion para actualizar el inventario	
class inventario_editar(generic.UpdateView):
	template_name   = 'dashboard/form_inventario_editar.html'
	model           = Inventario
	fields          = '__all__'
	success_url     = '../../../inventario/buscar/'


#ALMACEN
#Funcion para agregar un almacen
def almacen(request):
	form = FormAlmacen(request.POST)
	if form.is_valid():
		form.save()
		form = FormAlmacen()
	return render(request,"dashboard/form_almacen.html",{'form': form})

#Funcion para editar un almacen
class almacen_editar(generic.UpdateView):
	template_name   = 'dashboard/form_almacen_editar.html'
	model           = Almacen
	fields          = '__all__'
	success_url     = '../../../almacen/buscar/'	

#funcion para buscar un almacen por zona
def almacen_buscar(request):
	queryset = Almacen.objects.all()
	datos = []
	if request.method == 'GET':
		filtro = request.GET.get('filtro')
		if filtro is not None:
			print(filtro)
			data =  Almacen.objects.filter(Q(Almacen__icontains = filtro))
			for dt in data:
				datos.append({"almacen": str(dt.almacen), 'zona': str(dt.zona)})
		else:
			return render(request, 'dashboard/form_almacen_buscar.html',{'form': queryset})

	return HttpResponse(str(datos))	