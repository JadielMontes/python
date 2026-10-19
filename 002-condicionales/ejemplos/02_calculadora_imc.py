# LABORATORIO 2 - 02: IMC educativo (no es diagnostico)
peso = float(input("Peso en kg: "))
altura = float(input("Altura en metros: "))
if peso <= 0 or altura <= 0:
    print("Error: El peso y la altura deben ser mayores que cero.")
else:
    imc = peso / (altura ** 2)
    print("IMC: ", round(imc, 2))
    if imc < 18.5:
        print("Bajo")
    elif imc < 25:
        print("Habitual")
    else:
        print("Alto") 

# TAREA 1: Evitar dividir entre cero o valores negativos.
# TAREA 2: Calcular IMC = peso / (altura ** 2).
# TAREA 3: Mostrar IMC con dos decimales.
# TAREA 4: Mostrar 'bajo', 'habitual' o 'alto' con limites 18.5 y 25.
