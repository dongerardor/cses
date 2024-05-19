""" 
A Gray code is a list of all 2^n bit strings of length n, 
where any two successive strings differ in exactly one bit 
(i.e., their Hamming distance is one).
Your task is to create a Gray code for a given length n.

INPUT
The only input line has an integer n.

OUTPUT
Print 2^n lines that describe the Gray code. You can print any valid solution.
Constraints

1 <= n <= 16

Example
Input:
2

Output:
00
01
11
10


def is_power_of_two(n):
    return n > 0 and (n & (n - 1)) == 0

# Pruebas
print(is_power_of_two(1))  # True
print(is_power_of_two(2))  # True
print(is_power_of_two(3))  # False
print(is_power_of_two(4))  # True
print(is_power_of_two(5))  # False

"""

n = int(input())

columns = n
rows = 2 ** n
number_list = [0] * columns

# Crear el string binario con el ancho dinámico
initial_num = format(0, '0{}b'.format(columns))

def get_next_head_item(num_list, row):
    row_bin = bin(row).lstrip('0b')
    last_1_index = row_bin.rfind("1")
    last_1_col = len(row_bin) - last_1_index if last_1_index != -1 else None

    if(last_1_col):
        index_to_modify = len(num_list) - last_1_col
        value_to_modify = num_list[index_to_modify]
        new_value = 1 if value_to_modify == 0 else 0
        num_list[index_to_modify] = new_value
    return num_list


for i in range(0, rows, 4):
    number_list = get_next_head_item(number_list, i)
    print(''.join(map(str, number_list)))

    if len(number_list) > 0:
        number_list[-1] = 1 if number_list[-1] == 0 else 0
        print(''.join(map(str, number_list)))

    if len(number_list) > 1:
        number_list[-2] = 1 if number_list[-2] == 0 else 0
        print(''.join(map(str, number_list)))

        number_list[-1] = 1 if number_list[-1] == 0 else 0
        print(''.join(map(str, number_list)))