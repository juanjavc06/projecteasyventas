from django.urls import path
from sellpoint import views


urlpatterns = [

    path('login/', views.login ,name="login"),
    path('dashboard/', views.index ,name="dashboard"),
    path('', views.index),
    #PUNTO DE VENTA
    path('sellpoint/', views.startSellPoint,name="sellpoint"),

    #Categorias de Productos
    path('categorias/nuevo/', views.form_categorias_view, name="categoria_nueva_view"),

    #Productos
    path('productos/nuevo/', views.form_productos_view, name="producto_nuevo"),
    path('productos/buscar/', views.productos_buscar, name="producto_buscar"),

    path('productos/editar/<int:pk>/', views.form_productos_editar.as_view(), name="productos_editar"),
    path('productos/getbyid', views.get_products_by_id,name="productos_getbyid"),


    #PROVEEDORES POR PRODUCTO
    path('productos/proveedores/<int:id>/',views.form_productos_proveedores,name='proveedores_producto'),
    path('productos/proveedores_eliminar/<int:id>/',views.eliminar_proveedor_producto,name='eliminar_proveedor_producto'),

    #Usuarios

    path('productos/editar/<int:pk>/', views.form_productos_editar.as_view(), name="productos_editar"),

    path('proveedores/nuevo/', views.form_proveedores_view, name="proveedor_nuevo"),
    path('proveedores/', views.proveedores_buscar, name="proveedores_buscar"),
    path('proveedores/editar/<int:pk>/', views.form_proveedores_editar.as_view(), name="proveedores_editar"),

    path('usuarios/nuevo/',views.usuario, name="usuarios_nuevo"),
    path('usuarios/buscar/',views.usuarios_buscar,name="usuarios_buscar"),
    path('usuarios/editar/<int:pk>',views.usuario_editar.as_view(),name="usuarios_editar"),

    path('zona/nueva/',views.zona,name="zona_nueva"),

    path('almacen/',views.almacen,name="almacen"),
    path('almacen/nuevo/',views.almacen, name="almacen_nuevo"),
    path('almacen/editar/<int:pk>',views.almacen_editar,name="almacen_editar"),

    path('inventario/nuevo/',views.inventario,name="inventario_nuevo"),
    path('inventario/buscar/',views.inventario_buscar,name="inventario_buscar"),
    path('inventario/editar/<int:pk>',views.inventario_editar.as_view(),name="inventario_editar"),

]

#pip install django-widget-tweaks