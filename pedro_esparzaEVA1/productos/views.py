from django.shortcuts import render


# Productos organizados por categoría
productos_por_categoria_dict = {
    'Electronica': [
        {'id': 1, 'nombre': 'Laptop', 'descripcion': 'Laptop potente', 'imagen': 'laptop.jpg'},
        {'id': 2, 'nombre': 'Teléfono', 'descripcion': 'Smartphone avanzado', 'imagen': 'telefono.jpg'}
    ],
    'Juguetes': [
        {'id': 3, 'nombre': 'Peluche', 'descripcion': 'Peluche suave', 'imagen': 'peluche.jpg'},
        {'id': 4, 'nombre': 'Lego', 'descripcion': 'Set de construcción Lego', 'imagen': 'lego.jpg'}
    ],
    'Ropa': [
        {'id': 5, 'nombre': 'Camiseta', 'descripcion': 'Camiseta de algodón', 'imagen': 'camiseta.jpg'},
        {'id': 6, 'nombre': 'Chaqueta', 'descripcion': 'Chaqueta de cuero', 'imagen': 'chaqueta.jpg'}
    ]
}

def index(request):
    """Vista de la página de inicio, que muestra las categorías disponibles."""
    categorias = productos_por_categoria_dict.keys()  # Obtener categorías automáticamente
    return render(request, 'productos/index.html', {'categorias': categorias})

def productos_por_categoria_view(request, categoria):
    """Vista que muestra los productos de una categoría específica."""
    productos = productos_por_categoria_dict.get(categoria, [])
    if not productos:
        return render(request, 'productos/404.html', status=404)  # Página no encontrada si no hay productos

    return render(request, 'productos/categoria.html', {'categoria': categoria, 'productos': productos})

def usuario(request):
    """Vista que muestra la información del usuario."""
    context = {
        'id': 1,  
        'nombre': 'Pedro Esparza',
        'email': 'pedroesparzavera@gmail.com',
    }
    return render(request, 'productos/usuario.html', context)

def productos(request):
    """Vista que muestra todos los productos organizados por categoría."""
    return render(request, 'productos/productos.html', {'productos': productos_por_categoria_dict})

def descripcion_producto(request, categoria, producto_id):
    """Vista que muestra la descripción de un producto específico."""
    productos = productos_por_categoria_dict.get(categoria, [])
    producto = next((p for p in productos if p['id'] == producto_id), None)

    if producto is None:
        return render(request, 'productos/404.html', status=404)  # Manejo de producto no encontrado

    return render(request, 'productos/descripcion_producto.html', {'producto': producto, 'categoria': categoria})
