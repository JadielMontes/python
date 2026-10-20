# LABORATORIO PUENTE - Filtrar nombres por extension

archivos = ["factura.xml", "ventas.csv", "PEDIDO.XML", "notas.txt", "inventario.xml"]
print("Lista completa de archivos:", archivos)
for nombre in archivos:
    print(nombre)
print("Archivos con extension .xml:")
for nombre in archivos:
    if nombre.lower().endswith(".xml"):
        print(nombre)
print("Número de archivos con extension .xml:", len([nombre for nombre in archivos if nombre.lower().endswith(".xml")]))
# TAREA 1: Muestra solo los nombres que terminan en .xml.
# TAREA 2: Haz que tambien reconozca .XML.
# TAREA 3: Cuenta cuantos XML aparecen.
