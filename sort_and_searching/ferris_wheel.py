"""
Input:
4 10
7 2 3 9
Output:
3

Input:
3 10
1 2 3
Output:
2

Input:
10 2
1 2 2 1 1 2 2 2 2 2
Output:
9
"""

children_qty, max_weight = map(int, input().split())
weights = sorted(map(int, input().split()), reverse=True)
gondolas = 0

i = 0
j = len(weights) - 1
while i <= j:
    heavier = weights[i]
    lighter = weights[j]
    if heavier <= max_weight:
        gondolas += 1
        i += 1

    if heavier + lighter <= max_weight:
        j -= 1

print(gondolas)
