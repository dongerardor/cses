input = int(input())

total = (input * (input + 1)) / 2

set_half_a = set()
set_half_b = set()
half = 0

if total % 2 == 0:
    print("YES")

    num = input
    middle = total / 2
    while num > 0:
        if half + num <= middle:
            half += num
            set_half_a.add(num)
        else:
            set_half_b.add(num)
        num -= 1
    
    print(len(set_half_a))
    print(' '.join(map(str, set_half_a)))
    print(len(set_half_b))
    print(' '.join(map(str, set_half_b)))

else:
    print("NO")
