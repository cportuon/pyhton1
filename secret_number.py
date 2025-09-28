secret_number = 777

print(
"""
+================================+
| ¡Bienvenido a mi juego, muggle!|
| Introduce un número entero     |
| y adivina qué número he        |
| elegido para ti.               |
|¿Cuál es el número secreto?     |
+================================+
""")
number = int(input("Ingresa un número entero: "))

while number != secret_number:
    print("¡Ja, ja! ¡Estás atrapado en mi bucle!")
    number = int(input("Ingresa otro número entero: "))
else:
    print("Excelente, el número secreto es: ", number, "\n¡Bien hecho, muggle! Eres libre ahora.")

