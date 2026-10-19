# RETO EXTRA: calculadora de envio de TechStore.
numero = float(input("Ingresa el subtotal de la compra: "))
ciudad = input("Ingresa la ciudad (Quito u otra): ").strip().lower()


if numero >= 100:
    envio = 0
elif numero < 100 and ciudad == "quito":
    envio = 3
else:
    envio = 6

total = numero + envio
print(f"Subtotal: ${numero:.2f}")
print(f"Costo de envío: ${envio:.2f}")
print(f"Total a pagar: ${total:.2f}")


# Pide el subtotal de compra y la ciudad (Quito u otra).
# Si subtotal >= 100: envio gratis.
# Si subtotal < 100 y ciudad es Quito: envio $3.
# Si subtotal < 100 y es otra ciudad: envio $6.
# Muestra subtotal, envio y total.
# EXTRA: admite "quito", "QUITO" y "Quito".
