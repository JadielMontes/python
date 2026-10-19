# LABORATORIO 2 - 08: RETO EXTRA DESDE CERO
nombre = input("Nombre: ")
edad = int(input("Edad: "))
autorizacion = input("¿Tiene autorización? (si/no): ").lower()
if edad >= 18 and autorizacion == 'si':
    print("te permito entrar my causin")
else:
    if edad < 18:
        print("Ingreso denegado: Debe ser mayor de edad.")
    elif autorizacion != 'si':
        print("Ingreso denegado: Se requiere autorización.")
        
# TAREA 1: Pedir nombre y edad.
# TAREA 2: Preguntar si tiene autorizacion (si/no).
# TAREA 3: Permitir ingreso solo si edad >= 18 Y autorizacion == 'si'.
# TAREA 4: Mostrar motivo cuando no se permita el ingreso.
# TAREA 5: Aceptar 'SI', 'Si' y 'si' usando .lower().
