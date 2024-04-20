"""
A permutation of integers 1,2,\ldots,n is called beautiful if there are no adjacent elements whose difference is 1.
Given n, construct a beautiful permutation if such a permutation exists.
Input
The only input line contains an integer n.
Output
Print a beautiful permutation of integers 1,2,\ldots,n. If there are several solutions, you may print any of them. If there are no solutions, print "NO SOLUTION".
Constraints

1 \le n \le 10^6

Example 1
Input:
5

Output:
4 2 5 3 1
Example 2
Input:
3

Output:
NO SOLUTION



import importlib
mod = importlib.import_module("_05_permutation")

mod.funcion() # llamar una func del modulo

mod = importlib.reload(mod)
"""


from array import array

def odd_number(n):
    return 2 * n + 1

def even_number(n):
    return 2 * n

arr_size = int(input())
arr_even_size = arr_size//2
arr_odds_size = arr_size//2 if arr_size % 2 == 0 else arr_size//2 + 1
arr_even = array('i', [even_number(_ + 1) for _ in range(arr_even_size)])
arr_odds = array('i', [odd_number(_) for _ in range(arr_odds_size)])
arr = arr_even + arr_odds

if len(arr) > 1 and len(arr) < 4:
    output = 'NO SOLUTION'
else:
    output = ' '.join(map(str, arr))

print(output)
