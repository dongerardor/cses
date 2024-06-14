""" 
Your task is to calculate the number of trailing zeros in the factorial n!.
For example, 20!=2432902008176640000 and it has 4 trailing zeros.


import math

num = int(input())
factorial = math.factorial(num)

factorial_string = str(factorial)
trailing_zeros = 0

counter = len(factorial_string) - 1
list_of_zeros = list()
while counter > 0:
    ch = factorial_string[counter]
    if ch == "0":
        list_of_zeros.append(ch)
    else:
        break

    counter -= 1

print(len(list_of_zeros))

"""

import math

num = int(input())
factorial = math.factorial(num)

trailing_zeros = 0
divider = 10

while factorial % divider == 0:
    trailing_zeros += 1
    divider *= 10

print(trailing_zeros)