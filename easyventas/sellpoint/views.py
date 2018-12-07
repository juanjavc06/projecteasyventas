from django.shortcuts import *
from django.db.models import Q
from django.core.serializers import *
from django.http import JsonResponse, HttpResponse
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_exempt
from django.views import generic

from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login as logearse

from .models  import *
from .forms   import *
from .reports import * 

import datetime
import json
# Create your views here. 

def index(request):
	if request.user.is_authenticated:
		queryset = Productos.objects.all()
		return render(request, "dashboard/dashboard.html", {"productos":queryset})
	else:
		return render(request, "forms/login.html",{"msg":"session"} )

def logout_view(request):
	logout(request)
	return render(request, "forms/login.html",{"msg":"session"} )

def login(request):
	if request.method == 'POST':
		username = request.POST.get("username")
		cantidad = request.POST.get("password")
		user = authenticate(username=username, password=cantidad)
		if user is not None:
			logearse(request, user)
			# A backend authenticated the credentials
			return redirect('dashboard')
		else:
			# No backend authenticated the credential
			return render(request, "forms/login.html",{"msg":"login"} )
	else:
		return render(request, "forms/login.html")

def startSellPoint(request):
	return render(request, "sellpoint/sellpoint.html")

def producto_en_existencia(request):
	if request.user.is_authenticated:
		if request.method == 'GET':
			producto = request.POST.get("id")
			cantidad = request.POST.get("cantidad")
			en_existencia = Inventario.objects.filter(producto=producto).order_by('-id')
			
			if en_existencia.count() > 0 and en_existencia.existencias > int(cantidad):
				return HttpResponse("1")
			else:
				return HttpResponse("0")
		else:
			return HttpResponse("NO IDENTIFICADO")
	else:
		return render(request, "forms/login.html",{"msg":"session"} )

def generar_venta(request):
	if request.user.is_authenticated:
		if request.method == 'POST':
			objects = json.loads(request.POST.get("compra"))
			errors = []

			impuesto = float(request.POST.get("impuesto"))
			subtotal = float(request.POST.get("subtotal"))
			print(impuesto)
			print(objects)
			venta = Ventas(sub_total=float(subtotal),total=float(impuesto+subtotal),impuestos=impuesto,cliente=get_object_or_404(Proveedores_Clientes,id=1))
			venta.save()
			for x in range(0,len(objects)):
				print (objects[x])
				print (objects[x]['descripcion'])
				venta_detalle = Ventas_Detalle(
					venta   	   = venta,
					producto	   = get_object_or_404(Productos,id=objects[x]['id']),
					cantidad	   = objects[x]['cantidad'],
					total_producto = (float(objects[x]['cantidad']) * float(objects[x]['precio']) )
				)
				venta_detalle.save()
				#debemos crear el objeto inventario en caso de no existir
				inv = Inventario.objects.filter(producto=objects[x]['id']).order_by('-id')[:1]
				inv, creado = Inventario.objects.get_or_create(producto=venta_detalle.producto,defaults={'existencias':0,'zona': get_object_or_404(Zona,id=1) ,'producto': venta_detalle.producto})
				if not creado:
					inv.existencias = inv.existencias -  (float(objects[x]['cantidad']))
				else:
					#objects[x]['id']
					producto = venta_detalle.producto
					inv.existencias = 0,
					inv.producto = producto,
					inv.zona = get_object_or_404(Zona,id=1)
					
				inv.save()
				movimiento = Movimientos(
						tipo = "Venta",
						producto = venta_detalle.producto.nombre,
						cantidad = venta_detalle.cantidad,
						zona=get_object_or_404(Zona,id=1)
					)
				#return HttpResponse(request)
		return HttpResponse(request)
	else:
		return render(request, "forms/login.html",{"msg":"session"} )



def form_categorias_view(request):
	if request.user.is_authenticated:
		form = FormCategoria_Productos(request.POST)
		if request.method == 'POST':
			if form.is_valid():
				form.save()
				form = FormCategoria_Productos()
		queryset = Categoria_Productos.objects.all()
		context = {	'form':form	,'lista':queryset}
		return render(request,"dashboard/form_categoria_productos.html", context)
	else:
		return render(request, "forms/login.html",{"msg":"session"} )

#-------------------PRODUCTOS-------------------------------

def form_productos_view(request):
	if request.user.is_authenticated:
		form = FormProductos(request.POST)
		if form.is_valid():
			form.save()
			form = FormProductos()

		context = {	'form':form	}
		return render(request,"dashboard/form_productos.html", context)
	else:
		return render(request, "forms/login.html",{"msg":"session"} )

def ultimos_productos(request):
	if request.user.is_authenticated:
		queryset = Productos.objects.all()
		print(queryset)
		return render(request, "forms/ultimos_productos.html", {"productos": queryset})
	else:
		return render(request, "forms/login.html",{"msg":"session"} )

def productos_buscar(request):
	if request.user.is_authenticated:
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
	else:
		return render(request, "forms/login.html",{"msg":"session"} )

def get_products_by_id(request):
	if request.user.is_authenticated:
		queryset = Productos.objects.all()
		datos = []
		if request.method == 'GET':
			id_ = request.GET.get('id')
			if id_ is not None:
				data =  Productos.objects.filter(Q(id__icontains = id_))[:10]
				for dt in data:
					datos.append({"id": int(dt.id),"nombre": str(dt.nombre), 'descripcion': str(dt.descripcion), 'precio':str(dt.precio), 'unidad_medida':str(dt.unidad_medida)})
			else:
				HttpResponse("SETDATA")
		return HttpResponse(str(datos))
	else:
		return render(request, "forms/login.html",{"msg":"session"} )

class form_productos_editar(generic.UpdateView):
    template_name = 'dashboard/form_productos_editar.html'
    model = Productos
    fields = '__all__'
    success_url = '../../../productos/buscar/'

def contadorProductos(request):
	queryset = Productos.all()
	len(queryset)
	for obj in queryset:
		pass 

		
#-----------------PROVEEDORES---------------
def form_proveedores_view(request):
	if request.user.is_authenticated:
		form = FormProveedores_Clientes(request.POST)
		if form.is_valid():
			form.save()
			form = FormProveedores_Clientes()

		context = {	'form':form	}
		return render(request,"dashboard/form_proveedores_clientes.html", context)
	else:
		return render(request, "forms/login.html",{"msg":"session"} )

def proveedores_buscar(request):
	if request.user.is_authenticated:
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
	else:
		return render(request, "forms/login.html",{"msg":"session"} )


class form_proveedores_editar(generic.UpdateView):
    template_name = 'dashboard/form_proveedor_editar.html'
    model = Proveedores_Clientes
    fields = '__all__'
    success_url = '../../../proveedores/'


#------------RELACION PRODUCTOS PROVEEDORES

def form_productos_proveedores(request,id):
	if request.user.is_authenticated:
		producto 	= get_object_or_404(Productos,id=id)
		proveedores = Productos_Proveedores.objects.filter(producto__id=producto.id)
		context 	= {'producto':producto, 'proveedores': proveedores}
		return render(request, 'dashboard/form_productos_proveedores.html',context)
	else:
		return render(request, "forms/login.html",{"msg":"session"} )

@csrf_exempt
def guardar_proveedores_producto(request):
	if request.user.is_authenticated:
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
	else:
		return render(request, "forms/login.html",{"msg":"session"} )


def eliminar_proveedor_producto(request,id):
	pass

#------------ORDEN DE COMPRA
@csrf_exempt
def form_orden_compra(request):
	if request.user.is_authenticated:
		if request.method == "GET":
			form = FormCompras()
			context = {	'form':form	}
			return render(request,"dashboard/form_compras.html", context)
		else:

			objects = json.loads(request.POST.get('detalles'))
			print(objects)
			compra = Compras()
			compra.sub_total =request.POST.get('subtotal') 
			compra.impuestos =request.POST.get('impuestos') 
			compra.fecha_entrega = request.POST.get('fechaEntrega')
			compra.total = request.POST.get('total')
			compra.proveedor =  get_object_or_404(Proveedores_Clientes,rfc=request.POST.get('proveedorRFC'))

			compra.save()
			print(compra.id)
			for detalles in objects:
				detalle = Compras_Detalle()
				detalle.compra = compra
				#print(detalles['producto'])
				detalle.producto = get_object_or_404(Productos,nombre=detalles['producto'])
				detalle.cantidad = detalles['cantidad']
				detalle.total_producto = detalles['total_detalle']
				detalle.save()
				#print(detalle.id)
				#debemos aumentar el inventario del articulo
				inv, creado = Inventario.objects.get_or_create(producto=detalle.producto,defaults={'existencias':0,'zona': get_object_or_404(Zona,id=1) ,'producto': detalle.producto})
				print(creado )
				print('creado ', inv)
				if creado:
					inv.existencias = detalle.cantidad
					inv.producto = detalle.producto
					inv.zona 	 = get_object_or_404(Zona,id=1)
				else:
					inv.existencias = inv.existencias +detalle.cantidad
				inv.save()
				#se genera el movimiento
				movimiento = Movimientos()
				movimiento.tipo = 'Compra'
				movimiento.producto = detalle.producto
				movimiento.cantidad = detalle.cantidad
				movimiento.zona = inv.zona
				movimiento.save()
			return HttpResponse('Guardado con Exito')
		return HttpResponse('Error al guardar.')
	else:
		return render(request, "forms/login.html",{"msg":"session"} )


#-------------------------Seccion Jenny -------------------------------------------
# #ZONA
def zona(request):
	if request.user.is_authenticated:
		form = FormZona(request.POST)
		if form.is_valid():
			form.save()
			form = FormZona()
		return render(request,"dashboard/form_zona.html",{'form': form})
	else:
		return render(request, "forms/login.html",{"msg":"session"} )

#Funcion para actualizar las zonas
class zona_editar(generic.UpdateView):
	template_name   = 'dashboard/form_zona_editar.html'
	model           = Zona
	fields          = '__all__'
	success_url     = '../../../zona/buscar/'

def zona_buscar(request):
	if request.user.is_authenticated:
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
	else:
		return render(request, "forms/login.html",{"msg":"session"} )

#CORTE
def crear_corte(request):
	if request.user.is_authenticated:
		form = FormCortes(request.POST)
		if form.is_valid():
			form.save()
			form = FormCortes()
		return render(request,"dashboard/corte.html",{'form': form})
	else:
		return render(request, "forms/login.html",{"msg":"session"} )


#INVENTARIO
#Funcion para dar de alta inventario
def inventario(request):
	if request.user.is_authenticated:
		form = FormInventario(request.POST)
		if form.is_valid():
			form.save()
			form = FormInventario()
		return render(request,"dashboard/form_inventario.html",{'form':form})
	else:
		return render(request, "forms/login.html",{"msg":"session"} )

#Funcion para buscar inventario por producto
def inventario_buscar(request):
	if request.user.is_authenticated:
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
	else:
		return render(request, "forms/login.html",{"msg":"session"} )

#Funcion para actualizar el inventario	
class inventario_editar(generic.UpdateView):
	template_name   = 'dashboard/form_inventario_editar.html'
	model           = Inventario
	fields          = '__all__'
	success_url     = '../../../inventario/buscar/'


#ALMACEN
#Funcion para agregar un almacen
def almacen(request):
	if request.user.is_authenticated:
		form = FormAlmacen(request.POST)
		if form.is_valid():
			form.save()
			form = FormAlmacen()
		return render(request,"dashboard/form_almacen.html",{'form': form})
	else:
		return render(request, "forms/login.html",{"msg":"session"} )

#Funcion para editar un almacen
class almacen_editar(generic.UpdateView):
	template_name   = 'dashboard/form_almacen_editar.html'
	model           = Almacen
	fields          = '__all__'
	success_url     = '../../../almacen/buscar/'	

#funcion para buscar un almacen por zona
def almacen_buscar(request):
	if request.user.is_authenticated:
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
	else:
		return render(request, "forms/login.html",{"msg":"session"} )



#SELL POINT DEF
def startSellPoint(request):
	if request.user.is_authenticated:
		return render(request, "sellpoint/sellpoint.html")		
	else:
		return render(request, "forms/login.html",{"msg":"session"} )

#------------------------------------------REPORTES--------------------------------------------
def ReporteProductos(request):
	if request.user.is_authenticated:
		resp = HttpResponse(content_type='application/pdf')
		queryset = Productos.objects.all()
		context = {    'productos':queryset}
		return generate_pdf('reportes/reporte_productos.html', file_object=resp,context=context)
	else:
		return render(request, "forms/login.html",{"msg":"session"} )

def ReporteCompras(request):
	if request.user.is_authenticated:
		resp= HttpResponse(content_type="application/pdf")
		queryset = Compras.objects.all()
		context = { 'compras':queryset}
		return generate_pdf('reportes/reporte_compras.html',file_object=resp,context=context)
	else:
		return render(request, "forms/login.html",{"msg":"session"} )

def ReporteVentas(request):
	if request.user.is_authenticated:
		resp = HttpResponse(content_type="application/pdf")
		queryset = Ventas.objects.all()
		context= {'ventas': queryset}
		return generate_pdf('reportes/reporte_ventas.html',file_object=resp,context=context)
	else:
		return render(request, "forms/login.html",{"msg":"session"} )

def MasVendidos(request):
	if request.user.is_authenticated:
		queryset = Ventas_Detalle.objects.all().order_by('total_producto')
		context= {'masvendido': queryset}
		return generate_pdf('reportes/productos_mas_vendidos.html',file_object=resp,context=context)
	else:
		return render(request, "forms/login.html",{"msg":"session"} )



def ReporteInventario(request):
	if request.user.is_authenticated:
		resp = HttpResponse(content_type="application/pdf")
		queryset = Inventario.objects.all()
		context= {'inventario': queryset}
		return generate_pdf('reportes/reporte_inventario.html',file_object=resp,context=context)
	else:
		return render(request, "forms/login.html",{"msg":"session"} )



#------------CORTE DE CAJA

def consultarCorte(request):
	#validamos que exista algun corte para tomar esa fecha
	fechaInicial = Corte.objects.all().order_by('-fecha')[:1]
	print(fechaInicial)
	if not fechaInicial:
		fechaInicial =  datetime.date.today()
		print(fechaInicial)
	else :
		fechaInicial = fechaInicial.fecha
	print(fechaInicial)
	ventas = Ventas.objects.filter(fecha__icontains = fechaInicial)
	print(ventas)

	return render(request,"dashboard/form_corte.html",{'ventas':ventas})

