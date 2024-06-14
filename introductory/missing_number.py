""" 
You are given all numbers between 1,2,\ldots,n except one. Your task is to find the missing number.
Input
The first input line contains an integer n.
The second line contains n-1 numbers. Each number is distinct and between 1 and n (inclusive).
Output
Print the missing number.
Constraints

2 <= n <= 2 \cdot 10^5

Example
Input:
5
2 3 1 5

Output:
4


import importlib
modulo = importlib.import_module("_02_missing_number")

modulo.funcion() # llamar una func del modulo

modulo = importlib.reload(modulo)

 """

n = int(input())
numbers = input()

numbers_list = [int(n) for n in numbers.split()]
sum = 0
sum_total = 0

for num in range(1, n + 1):
    sum_total += num

for num in numbers_list:
    sum += num

result = sum_total - sum

print(result)
