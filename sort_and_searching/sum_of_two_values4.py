# total = 3
# values = values = list(map(int, "1 1 1 1 1 1 1 1 1 1 1 1 1".split()))


_, total = map(int, input().split())
values = list(map(int, input().split()))
new_values = []

def get_pairs():
    for i, num in enumerate(values):
        lower = num
        higher = total - lower
        if higher in new_values:
            lower_index = i
            higher_index = new_values.index(higher)
            return (higher_index, lower_index)
        
        new_values.append(num)
    
    return None

pairs = get_pairs()
if pairs:
    higher_index, lower_index = pairs
    print(f"{higher_index + 1} {lower_index + 1}")
else:
    print(f"IMPOSSIBLE")