# Leer número de bloques para hacer alturas de una piramide

blocks = int(input("Ingresa el número de bloques: "))

height = 0 
needed = 1 # bloques necesarios que la primera capa

while blocks >= needed:
    blocks -= needed
    height += 1
    needed += 1


print("La altura de la pirámide:", height)

