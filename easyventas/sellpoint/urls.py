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

    #Usuarios
    path('usuarios/nuevo/',views.usuario, name="usuarios_nuevo"),
    path('zona/nueva/',views.zona,name="zona_nueva"),


]

#pip install django-widget-tweaks