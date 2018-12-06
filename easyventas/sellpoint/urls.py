from django.urls import path
from sellpoint import views

from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    
    path('', views.index,name="dashboard"),
    #PUNTO DE VENTA
    path('sellpoint/', views.startSellPoint,name="sellpoint"),
    path('sellpoint/comprar', csrf_exempt(views.generar_venta),name="sellpoint_comprar"),

    #Categorias de Productos
    path('categorias/nuevo/', views.form_categorias_view, name="categoria_nueva_view"),

    #Productos
    path('productos/nuevo/', views.form_productos_view, name="productos_nuevo"),
    path('productos/buscar/', views.productos_buscar, name="producto_buscar"),
    path('productos/editar/<int:pk>/', views.form_productos_editar.as_view(), name="productos_editar"),
    path('productos/getbyid', views.get_products_by_id,name="productos_getbyid"),

    #PROVEEDORES POR PRODUCTO
    path('productos/proveedores/<int:id>/',views.form_productos_proveedores,name='proveedores_producto'),
    path('productos/proveedores_eliminar/<int:id>/',views.eliminar_proveedor_producto,name='eliminar_proveedor_producto'),
    path('productos/proveedores_guardar/',views.guardar_proveedores_producto, name='guardar_proveedores_producto'),
    path('productos/esta_existencia/',views.producto_en_existencia, name='productos_esta_existencia'),
    
    #Usuarios

    path('productos/editar/<int:pk>/', views.form_productos_editar.as_view(), name="productos_editar"),


    path('proveedores/nuevo/', views.form_proveedores_view, name="proveedor_nuevo"),
    path('proveedores/', views.proveedores_buscar, name="proveedores_buscar"),
    path('proveedores/editar/<int:pk>/', views.form_proveedores_editar.as_view(), name="proveedores_editar"),

    #orden de compra
    path('compras/nuevo/', views.form_orden_compra, name="nueva_orden_compra"),
    
    #zona
    path('zona/nueva/',views.zona,name="zona_nueva"),
    path('zona/buscar/',views.zona_buscar,name="zona_buscar"),
    path('zona/editar/<int:pk>/',views.zona_editar.as_view(),name="zona_editar"),

    #almacen
    path('almacen/',views.almacen,name="almacen"),
    path('almacen/nuevo/',views.almacen, name="almacen_nuevo"),
    path('almacen/buscar/',views.almacen_buscar,name="almacen_buscar"),
    path('almacen/editar/<int:pk>/',views.almacen_editar.as_view(),name="almacen_editar"),

    #inventario
    path('inventario/nuevo/',views.inventario,name="inventario_nuevo"),
    path('inventario/buscar/',views.inventario_buscar,name="inventario_buscar"),
    path('inventario/editar/<int:pk>/',views.inventario_editar.as_view(),name="inventario_editar"),

    #reportes
    path('reporte/productos/',views.ReporteProductos,name="reporte_productos"),
    path('reportes/compras/',views.ReporteCompras,name="reporte_compras"),
    path('reporte/ventas/',views.ReporteVentas,name="reporte_ventas"),
    path('reporte/inventario/',views.ReporteInventario,name="reporte_inventario"),
    path('reporte/productos/masvendidos',views.MasVendidos,name="reporte_productos_masvendidos"),

]

#pip install django-widget-tweaks