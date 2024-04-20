"""

You are given an array of n integers. You want to modify the array so that it is increasing, i.e., every element is at least as large as the previous element.
On each move, you may increase the value of any element by one. What is the minimum number of moves required?
Input
The first input line contains an integer n: the size of the array.
Then, the second line contains n integers x_1,x_2,\ldots,x_n: the contents of the array.
Output
Print the minimum number of moves.
Constraints

1 \le n \le 2 \cdot 10^5
1 \le x_i \le 10^9

Example
Input:
5
3 2 5 1 7

Output:
5

Example 2
10
6 10 4 10 2 8 9 2 7 7

Output
31




import importlib
mod = importlib.import_module("_04_increasing_array")

mod.funcion() # llamar una func del modulo

mod = importlib.reload(mod)

"""
# 5
# 3 2 5 1 8

from array import array

arr_size = int(input())
arr = array('i', [int(num) for num in input().split()])
updated_arr = array('i', [0] * arr_size)


for i, num in enumerate(arr):
    updated_num = num
    if i > 0:
        prev = updated_arr[i - 1]
        if prev > num:
            updated_num = prev

    updated_arr[i] = updated_num

operation_arr = array('i', [a - b for a, b in zip(updated_arr, arr)])

moves = sum(operation_arr)

print(moves)