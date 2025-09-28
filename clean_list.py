'''
Tengo una lista de números enteros y 
quiero borrar de la lista 
los números que esten repetidos
'''
my_list = [2, 8, 10, 59, 8, 8, 66, 4, 13, 2, 10, 59, 99]
new_list = []

for num in range(len(my_list)):
    if my_list[num] not in new_list:
        new_list.append(my_list[num])

print("La lista con elementos únicos: ", new_list)


# my_list = [2, 8, 10, 59, 8, 8, 66, 4, 13, 2, 10, 59, 99]
# find = True
# swap = my_list[0]
# count = 0
# len_list = len(my_list) 

# while find:
#     find = False
#     for i in range(len_list - 1):
#         if i == len_list - 1:
#             break
#         for j in range(len_list - 1):
#             if j == len_list - 1:
#                 swap = my_list[i + 1]
#                 break
#             if swap == my_list[j + 1]:
#                 find = True
#                 del my_list[j + 1]
#                 len_list -= 1
            
# print(my_list)