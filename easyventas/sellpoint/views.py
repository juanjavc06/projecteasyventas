from django.shortcuts import render
from django.views import generic
from django.db.models import Q
from django.views.decorators.csrf import csrf_exempt
from django.core.serializers import *
from django.shortcuts import *

from django.urls import reverse_lazy
import json

from django.http import JsonResponse, HttpResponse


from  .models import *
from .forms import * 

# Create your views here.


def index(request):
	queryset = Productos.objects.all()
	return render(request, "dashboard/dashboard.html", {"productos":queryset})

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

#-------------------PRODUCTOS-------------------------------

def form_productos_view(request):
	form = FormProductos(request.POST)
	if form.is_valid():
		form.save()
		form = FormProductos()

	context = {	'form':form	}
	return render(request,"dashboard/form_productos.html", context)

def ultimos_productos(request):
	print('cerdito :v')
	queryset = Productos.objects.all()
	print(queryset)
	return render(request, "forms/ultimos_productos.html", {"productos": queryset})

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
	print(request.GET)
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

def form_productos_proveedores(request,id):
	producto 	= get_object_or_404(Productos,id=id)
	proveedores = Productos_Proveedores.objects.filter(producto__id=producto.id)
	context 	= {'producto':producto, 'proveedores': proveedores}
	return render(request, 'dashboard/form_productos_proveedores.html',context)

@csrf_exempt
def guardar_proveedores_producto(request):
	print('entre a la funcion')
	if request.method == 'POST':
		print(request.POST.get('lista'))
		objects = json.loads(request.POST.get('lista'))
		print(objects)
		for proveedor in objects:
			print(proveedor['producto'])
			if proveedor['id'] != 0:
				prodProv = get_object_or_404(Productos_Proveedores,id=proveedor['id'])
			else:
				prodProv = Productos_Proveedores()
			prodProv.producto = get_object_or_404(Productos,nombre=proveedor['producto'])
			prodProv.proveedor = get_object_or_404(Proveedores_Clientes,rfc=proveedor['proveedor'])
			prodProv.cantidad = proveedor['cantidad']
			prodProv.costo_total = proveedor['precio']
			prodProv.save()
		return HttpResponse('Guardado con Exito')
	return HttpResponse('Error al procesar los datos')
		


def eliminar_proveedor_producto(request,id):
	pass

#------------ORDEN DE COMPRA

def form_orden_compra(request):`
	if request.method == "GET":
		form = FormCompras()
		context = {	'form':form	}
		return render(request,"dashboard/form_compras.html", context)
	else:
		objects = json.loads(request.POST.get('detalles'))
		print(objects)
		for detalles in objects:
			print(detalles['producto'])
			if detalles['id'] != 0:
				prodProv = get_object_or_404(Productos_detalleses,id=detalles['id'])
			else:
				prodProv = Productos_detalleses()
			prodProv.producto = get_object_or_404(Productos,nombre=detalles['producto'])
			prodProv.detalles = get_object_or_404(detalleses_Clientes,rfc=detalles['detalles'])
			prodProv.cantidad = detalles['cantidad']
			prodProv.costo_total = detalles['precio']
			prodProv.save()
		return HttpResponse('Guardado con Exito')








#-------------------------Seccion Jenny -------------------------------------------


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


#------------------------------------------REPORTES--------------------------------------------
#class Reporte_Productos(View):
#	def get(self,request,*args,**kwargs):
#		reporte=render_pdf("reportes/reporte_productos.html")
#		datos()
#		return HttpResponse(reporte,content_type="")
