# Cuál es el número mas grande de entre 3 números

# num1 = int(input("\n1 - Introduce el primer número: "))
# num2 = int(input("\n2 - Introduce el segundo número: "))
# num3 = int(input("\n3 - Introduce el tercer número: "))

# big_num = num1

# if num2 > big_num: big_num = num2
# elif num3 > big_num: big_num = num3

# print("\n****** El número más grande es: ", big_num, "******", end="\n\n")

# Una forma más simple de encontrar el número mas grande o el más pequeño

num1 = int(input())
num2 = int(input())
num3 = int(input())

largest_num = max(num1, num2, num3)

print("El número más grande es el: ", largest_num)
