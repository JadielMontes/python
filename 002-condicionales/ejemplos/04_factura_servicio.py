# LABORATORIO 2 - 04: Factura ficticia
horas = float(input("Horas de trabajo: "))
tarifa = 12.50
repuestos = float(input("Costo de repuestos: "))
if horas < 0 or repuestos < 0:
    print("Error: Las horas y los repuestos no pueden ser negativos.")
else:
    subtotal = horas * tarifa + repuestos
    if subtotal >= 100:
        descuento = subtotal * 0.08
    else:
        descuento = 0
    total = subtotal - descuento
    print(f"Subtotal: ${subtotal:.2f}")
    print(f"Descuento: ${descuento:.2f}")
    print(f"Total: ${total:.2f}")

# TAREA 1: Validar que horas y repuestos no sean negativos.
# TAREA 2: Si subtotal >= 100, aplicar 8% de descuento.
# TAREA 3: Mostrar subtotal, descuento y total con dos decimales.
