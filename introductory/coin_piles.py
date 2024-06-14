"""
You have two coin piles containing a and b coins.
On each move, you can either remove one coin
from the left pile and two coins from the right pile,
or two coins from the left pile and one coin from the right pile.

Your task is to efficiently find out if you can empty both the piles.

INPUT
The first input line has an integer t: the number of tests.
After this, there are t lines, each of which has two integers
a and b: the numbers of coins in the piles.

OUTPUT
For each test, print "YES" 
if you can empty the piles and
"NO" otherwise.

CONSTRAINTS

1 <= t <= 10 ** 5
0 <= a, b <= 10 ** 9

====================
EXAMPLE
====================
INPUT: 
3
2 1
2 2
3 3

OUTPUT:
YES
NO
YES
====================
"""

def coin_piles(piles):
    result = ''
    for couple in piles:
        coins = sum(couple)
        if coins % 3 == 0 and min(couple) >= max(couple) / 2:
            result += "YES\n"
        else:
            result += "NO\n"

    return result


if __name__ == "__main__":
    num = int(input())
    piles = []
    for _ in range(num):
        left, right = map(int, input().split())
        piles.append((left, right))

    result = coin_piles(piles)
    print(result)