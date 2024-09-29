from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('usuario/', views.usuario, name='usuario'),
    path('productos/', views.productos, name='productos'),
    path('productos/<str:categoria>/<int:producto_id>/', views.descripcion_producto, name='descripcion_producto'),  # Cambiado para incluir la categoría
    path('<str:categoria>/', views.productos_por_categoria_view, name='productos_por_categoria'),
]

