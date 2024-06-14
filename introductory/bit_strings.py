""" 
Your task is to calculate the number of bit strings of length n.
For example, if n=3, the correct answer is 8, 
because the possible bit strings are 
000, 001, 010, 011, 100, 101, 110, and 111.

INPUT
The only input line has an integer n.

OUTPUT
Print the result modulo 10^9+7.

CONSTRAINTS
1 <= n <= 10**6

====================
EXAMPLE
====================
INPUT: 3
OUTPUT: 8
====================
"""

def binary_string(num):
    return (1 << num) % 1000000007

if __name__ == "__main__":
    num = int(input())
    result = binary_string(num)
    print(result)