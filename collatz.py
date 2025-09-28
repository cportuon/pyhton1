"""
+-----------------------------------------------+
|                                               |
|           Hipótesis de Collatz                |
|                                               |
|                                               |
|                                               |
+-----------------------------------------------+
"""
c0 = int(input("Introduce un número que no sea negativo y que no sea cero: "))

counter = 0

while c0 != 1:              # Mientras sea distinto de 1
    if c0 % 2 == 1:         # Si es un número impar 
        c0 = 3 * c0 + 1
    else: c0 = c0 // 2      # Si es un número par
    print(c0)
    counter += 1
print("Pasos: ", counter)

