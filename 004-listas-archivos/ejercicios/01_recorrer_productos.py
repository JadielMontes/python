# LABORATORIO PUENTE - Recorrer una lista de productos

productos = ["Teclado", "Mouse", "Monitor", "Impresora", "Webcam"]
productos.append("Auriculares")
productos.append("Micrófono")
print("Lista completa de productos:", productos)
mensajes = [
    "Este producto es de alta calidad.",
    "Este producto tiene garantía de un año.",
    "Este producto es compatible con múltiples sistemas.",
    "Este producto es ideal para uso profesional.",
    "Este producto tiene un diseño ergonómico.",
    "Este producto ofrece un sonido nítido y claro.",
    "Este producto es perfecto para videos de YT."
]
for producto in productos:
    print("Producto:", producto)
    print("Mensaje:", mensajes[productos.index(producto)])

print("Número de productos:", len(productos))

# TAREA 1: Agrega dos productos a la lista.
# TAREA 2: Muestra un mensaje diferente para cada producto.
# TAREA 3: Al final muestra cuantos productos hay con len().
