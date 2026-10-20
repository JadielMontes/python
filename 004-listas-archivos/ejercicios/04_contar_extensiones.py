# LABORATORIO PUENTE - Contadores de extensiones

archivos = ["a.xml", "b.txt", "c.csv", "d.XML", "e.txt", "f.pdf"]
xml = 0
print("Lista completa de archivos:", archivos)
for nombre in archivos:
    if nombre.lower().endswith(".xml"):
        xml += 1
print("Número de archivos con extensión .xml:", xml)
print("XML:", xml)
print("TXT:", len([nombre for nombre in archivos if nombre.lower().endswith(".txt")]))
print("CSV:", len([nombre for nombre in archivos if nombre.lower().endswith(".csv")]))
print("PDF:", len([nombre for nombre in archivos if nombre.lower().endswith(".pdf")]))
# TAREA 1: Crea contadores para TXT y CSV.
# TAREA 2: Muestra los tres totales.
# TAREA 3: Cuenta los archivos de otras extensiones.
