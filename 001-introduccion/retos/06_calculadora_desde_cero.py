# RETO: construye una calculadora de dos numeros.
numero1 = float(input("Ingresa el primer número: "))
numero2 = float(input("Ingresa el segundo número: "))
operacion = input("Ingresa la operación (+, -, *, /): ")

banderaSivisonCero = False
if operacion == "+":
    resultado = numero1 + numero2
elif operacion == "-":  
    resultado = numero1 - numero2  
elif operacion == "*":
    resultado = numero1 * numero2
elif operacion == "/":
    if numero2 == 0:
        banderaSivisonCero = True
    else:
        resultado = numero1 / numero2

if(banderaSivisonCero): 
    print(f"Error: No se puede dividir entre cero.") 
else:
    print(f"El resultado de {numero1} {operacion} {numero2} es: {resultado}")


# Debe pedir dos numeros y una operacion (+, -, *, /).
# Muestra el resultado.
# Si se intenta dividir entre cero, muestra un aviso en lugar de fallar.
# EXTRA: muestra un mensaje si la operacion no existe.
