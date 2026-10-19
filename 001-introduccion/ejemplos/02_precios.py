# Calculadora de precios de TechStore
from wsgiref import validate


producto = input("Producto: ")
precio = float(input("Precio unitario: "))
cantidad = int(input("Cantidad: "))
subtotal = precio * cantidad
descuentoFijo = subtotal * 0.10
print("descuento fijo:", descuentoFijo)


porcentaje = int(input("porcentaje: "))

if 0 <= porcentaje <= 100:
    descuento = subtotal * porcentaje / 100
    total = subtotal - descuento
    print("Producto:", producto)
    print(f"Subtotal: ${subtotal:.2f}")
    print(f"Descuento: ${descuento:.2f}")
    print(f"Total: ${total:.2f}")
else : 

    print("mensaje de que no es valido")

# TAREA 1: aplica un descuento fijo del 10 %.
# TAREA 2: pide el porcentaje al usuario.
# TAREA 3: muestra subtotal, descuento y total con dos decimales.
