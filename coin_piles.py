""" 
3
2 1
2 2
3 3

(2, 1), (2, 2), (3, 3)

"""

# num = 3
# piles = [(2, 1), (2, 2), (3, 3)]

num = int(input())
piles = []
for _ in range(num):
    left, right = map(int, input().split())
    piles.append((left, right))

for couple in piles:
    coins = sum(couple)
    if coins % 3 == 0 and min(couple) >= max(couple) / 2:
        print("YES")
    else:
        print("NO")
