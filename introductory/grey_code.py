""" 
A Gray code is a list of all 2 ** n bit strings of length n, 
where any two successive strings differ in exactly one bit 
(i.e., their Hamming distance is one).
Your task is to create a Gray code for a given length n.

INPUT
The only input line has an integer n.

OUTPUT
Print 2 ** n lines that describe the Gray code. 
You can print any valid solution.

CONSTRAINTS

1 <= n <= 16

====================
EXAMPLE
====================
INPUT: 
2

OUTPUT:
00
01
11
10
====================
"""

n = int(input())

columns = n
rows = 2 ** n
number_list = [0] * columns

# Create binary string with dynamic width
# i.e.: columns = 3 -> '000'
initial_num = format(0, '0{}b'.format(columns))

def get_next_head_item(number_list, row):
    row_bin = bin(row).lstrip('0b')
    last_1_index = row_bin.rfind("1")
    last_1_col = len(row_bin) - last_1_index if last_1_index != -1 else None

    if(last_1_col):
        index_to_modify = len(number_list) - last_1_col
        value_to_modify = number_list[index_to_modify]
        new_value = 1 if value_to_modify == 0 else 0
        number_list[index_to_modify] = new_value
    return number_list


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
