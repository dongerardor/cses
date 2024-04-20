num = int(input())
print(num)
output = ''

for n in range(num):
    pair = input()
    pair_tuple = tuple(map(int, pair.split()))
    output += 'YES\n' if sum(pair_tuple) % 3 == 0 else 'NO\n'
    
print(output)