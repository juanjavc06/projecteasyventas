from django.urls import path
from sellpoint import views


urlpatterns = [

    path('login/', views.login ,name="login"),
    path('dashboard/', views.index ,name="dashboard"),
    path('', views.index),
    path('sellpoint/', views.startSellPoint,name="sellpoint"),
    path('categorias/nuevo/', views.form_categorias_view, name="categoria_nueva_view"),
    path('productos/nuevo/', views.form_productos_view, name="producto_nuevo"),
    path('usuarios/nuevo/',views.usuario, name="usuarios_nuevo"),
    path('zona/nueva/',views.zona,name="zona_nueva"),


]

#pip install django-widget-tweaks