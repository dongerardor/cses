import array

# Definir un array de enteros
# El primer argumento especifica el tipo de datos ('i' para enteros)
# El segundo argumento es una secuencia de valores enteros
""" arr = array.array('i', [1, 2, 3, 4, 5])

# Imprimir el array
print("Array original:", arr)

# Acceder a un elemento del array por índice
print("Elemento en el índice 2:", arr[2])

# Modificar un elemento del array por índice
arr[2] = 10
print("Array modificado:", arr)

# Calcular la longitud del array
print("Longitud del array:", len(arr))

# Añadir un elemento al final del array
arr.append(6)
print("Array con elemento añadido:", arr)

# Eliminar un elemento del array por valor
arr.remove(5)
print("Array con elemento eliminado:", arr)

# Iterar sobre los elementos del array
print("Iteración sobre el array:")
for elem in arr:
    print(elem) """





# arr2 = array.array('i', [1, 3, 5, 2, 4])  # Crear un array de enteros
# max_value = max(arr2)  # Encontrar el valor máximo en el array
# print(max_value)  # Imprimir el valor máximo



""" xx = 8

def lowering(num):
    if num > 0:
        print(num)
        return lowering(num - 1)
    else:
        return num

aa = lowering(xx)
print(aa) """



my_list = [1, 2, 3, 4, 5, 6, 7]

my_list_reversed = my_list[::-1]

print(my_list_reversed)

my_list_reversed2 = my_list[::-2]

print(my_list_reversed2)

my_list_reversed3 = my_list[3::-1]
print(my_list_reversed3)

last_index = len(my_list) - my_list[::-1].index(2) - 1
print(last_index)  # Output: 6


