"""
You are given an array of n integers. 
You want to modify the array so that it is increasing, 
i.e., every element is at least as large as the previous element.

On each move, you may increase the value of any element by one.

What is the minimum number of moves required?

INPUT
The first input line contains an integer n: the size of the array.
Then, the second line contains n integers x1, x2, ... ,xn: the contents of the array.

OUTPUT
Print the minimum number of moves.

CONSTRAINTS
1 <= n <= 2 * (10 ** 5)
1 <= xi <= 10 ** 9

====================
EXAMPLE
====================
INPUT:
5
3 2 5 1 7

OUTPUT:
5

====================
EXAMPLE 2
====================
INPUT:
10
6 10 4 10 2 8 9 2 7 7

OUTPUT:
31

"""

from array import array

def calculate_moves(arr):
    updated_arr = array('i', [0] * len(arr))
    for i, num in enumerate(arr):
        updated_num = num
        if i > 0:
            prev = updated_arr[i - 1]
            if prev > num:
                updated_num = prev

        updated_arr[i] = updated_num

    operation_arr = array('i', [a - b for a, b in zip(updated_arr, arr)])

    return sum(operation_arr)


if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    print(calculate_moves(arr))
