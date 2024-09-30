from django.shortcuts import render


productos_por_categoria_dict = {
    'LAPTOP': [
        {
            'id': 1,
            'nombre': 'Lenovo',
            'descripcion': 'NOTEBOOK LENOVO YOGA SLIM 7X SNAPDRAGON X ELITE 32GB RAM 1TB SSD 14.5” TOUCH OLED',
            'imagen': 'laptop/Lenovo/lenovo_yoga.jpg',
            'marca': 'Lenovo',
            'modelo': 'Yoga Slim 7X',
            'tipo_procesador': 'Snapdragon',
            'memoria_ram': '32GB',
            'disco_solido': '1TB SSD',
            'garantia': '1 año',
            'velocidad_procesador': '2.84 GHz',
            'tipo_memoria_ram': 'LPDDR4X',
            'tipo_pantalla': 'OLED',
            'tarjeta_grafica': 'Adreno',
            'cantidad_puerto_usb': 2,
            'cantidad_puertos_hdmi': 1,
            'unidad_optica': 'No',
            'tipo_bateria': 'Litio',
        },
        {
            'id': 3,
            'nombre': 'Acer',
            'descripcion': 'NOTEBOOK GAMER ACER ASPIRE 5 A515-58GM-56XX-1 INTEL CORE I5 16 GB RAM 512 GB SSD NVIDIA RTX 2050 15.6',
            'imagen': 'laptop/Acer_HP/acer_aspire5.jpg',
            'marca': 'Acer',
            'modelo': 'Aspire 5',
            'tipo_procesador': 'Intel Core i5',
            'memoria_ram': '16GB',
            'disco_solido': '512GB SSD',
            'garantia': '1 año',
            'velocidad_procesador': '4.4 GHz',
            'tipo_memoria_ram': 'DDR4',
            'tipo_pantalla': 'IPS',
            'tarjeta_grafica': 'NVIDIA RTX 2050',
            'cantidad_puerto_usb': 3,
            'cantidad_puertos_hdmi': 1,
            'unidad_optica': 'No',
            'tipo_bateria': 'Litio',
        },
        {
            'id': 4,
            'nombre': 'HP',
            'descripcion': 'NOTEBOOK GAMER HP VICTUS 15-FA1097LA INTEL CORE I7 16GB 1TB SSD NVIDIA RTX 4050 15.6',
            'imagen': 'laptop/Acer_HP/HP_victus.jpg',
            'marca': 'HP',
            'modelo': 'Victus 15',
            'tipo_procesador': 'Intel Core i7',
            'memoria_ram': '16GB',
            'disco_solido': '1TB SSD',
            'garantia': '1 año',
            'velocidad_procesador': '4.6 GHz',
            'tipo_memoria_ram': 'DDR4',
            'tipo_pantalla': 'IPS',
            'tarjeta_grafica': 'NVIDIA RTX 4050',
            'cantidad_puerto_usb': 4,
            'cantidad_puertos_hdmi': 1,
            'unidad_optica': 'No',
            'tipo_bateria': 'Litio',
        },
    ],
    
    'COMPONENTES': [
        {
            'id': 7,
            'nombre': 'MSI',
            'descripcion': 'TARJETA DE VIDEO MSI NVIDIA® GEFORCE® RTX™ 4060 VENTUS 2X BLACK OC, 8GB GDDR6, 128-BIT, PCI-E 4.0',
            'imagen': 'componentes/grafica_nvidia4060.jpeg',
            'marca': 'MSI',
            'modelo': 'GeForce RTX 4060',
            'velocidad': '2.76 GHz',  # Velocidad de la tarjeta
            'capacidad': '8GB GDDR6',  # Capacidad de memoria
            'interfaz': 'PCI-E 4.0',  # Tipo de interfaz
            'dimensiones': '242 x 112 x 40 mm',  # Dimensiones
            'garantia': '3 años',  # Garantía
        },
        {
            'id': 8,
            'nombre': 'GIGABYTE',
            'descripcion': 'TARJETA DE VIDEO GIGABYTE RADEON RX6900XT GAMING OC 16G 4K',
            'imagen': 'componentes/grafica_giga.jpg',
            'marca': 'GIGABYTE',
            'modelo': 'Radeon RX 6900 XT',
            'velocidad': '2.25 GHz',  # Velocidad de la tarjeta
            'capacidad': '16GB GDDR6',  # Capacidad de memoria
            'interfaz': 'PCI-E 4.0',  # Tipo de interfaz
            'dimensiones': '320 x 140 x 50 mm',  # Dimensiones
            'garantia': '3 años',  # Garantía
        },
        {
            'id': 9,
            'nombre': 'WD',
            'descripcion': 'DISCO DURO SSD 480GB',
            'imagen': 'componentes/ssd_wd.jpg',
            'marca': 'Western Digital',
            'modelo': 'WD Green SSD',
            'velocidad': '545 MB/s',  # Velocidad de lectura
            'capacidad': '480GB',  # Capacidad de almacenamiento
            'tipo': '2.5" SATA III',  # Tipo de unidad
            'garantia': '3 años',  # Garantía
        },
    ],
     'PERIFERICOS': [
        {
            'id': 10,
            'nombre': 'Maxell',
            'descripcion': 'PENDRIVE MAXELL FLIX 256GB 3.2',
            'imagen': 'perifericos/pen_maxell.jpg',
            'marca': 'Maxell',
            'modelo': 'Max_256',
            'capacidad': '256GB',
            'tipo_conexion': 'USB 3.2',
            'dimensiones': '60 x 18 x 9 mm',
            'garantia': '2 años',
        },
        {
            'id': 11,
            'nombre': 'Razer',
            'descripcion': 'MOUSE GAMER RAZER BASILISK V3 PRO INALÁMBRICO RECARGABLE',
            'imagen': 'perifericos/mouse_razer.jpg',
            'marca': 'Razer',
            'modelo': 'Razer zx98',
            'tipo_conexion': 'Inalámbrico',
            'tipo_bateria': 'Recargable',
            'dpi': '20,000 DPI',
            'cantidad_botones': 11,
            'garantia': '2 años',
        },
        {
            'id': 12,
            'nombre': 'Logitech',
            'descripcion': 'TECLADO LOGITECH ERGO K860 QWERTY ESPAÑOL COLOR NEGRO',
            'imagen': 'perifericos/teclado_logi.jpg',
            'marca': 'Logitech',
            'modelo': 'Logi_987',
            'tipo_conexion': 'Bluetooth',
            'tipo_bateria': '2 Pilas AAA',
            'layout': 'QWERTY Español',
            'dimensiones': '456 x 233 x 48 mm',
            'garantia': '3 años',
        }
    ],
}

def index(request):
    """Vista de la página de inicio, que muestra las categorías disponibles."""
    categorias = productos_por_categoria_dict.keys()  
    return render(request, 'productos/index.html', {'categorias': categorias})

def productos_por_categoria_view(request, categoria):
    """Vista que muestra los productos de una categoría específica."""
    productos = productos_por_categoria_dict.get(categoria, [])
    return render(request, 'productos/categoria.html', {'categoria': categoria, 'productos': productos})

def usuario(request):
    """Vista que muestra la información del usuario."""
    context = {
        'id': 1,  
        'nombre': 'Pedro Esparza',
        'email': 'pedroesparzavera@gmail.com',
        'carrera' : 'Analista Programador',
        'jornada' : 'Vespertina'
    }
    return render(request, 'productos/usuario.html', context)

def productos(request):
    """Vista que muestra todos los productos organizados por categoría."""
    return render(request, 'productos/productos.html', {'productos': productos_por_categoria_dict})

def descripcion_producto(request, categoria, producto_id):
    """Vista que muestra la descripción de un producto específico."""
    productos = productos_por_categoria_dict.get(categoria, [])
    producto = next((p for p in productos if p['id'] == producto_id), None)

    return render(request, 'productos/descripcion_producto.html', {'producto': producto, 'categoria': categoria})
