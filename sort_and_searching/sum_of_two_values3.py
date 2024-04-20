# total = 4
# values = values = list(map(int, "3 3 1 2".split()))

from array import array

_, total = map(int, input().split())
values = list(map(int, input().split()))
values_array = array('i', set(values))
values_sorted_array = sorted(values_array, reverse=True)

def get_pair(higher = None):
    if not higher:
        higher = values_sorted_array[0]

    lower_val = total - higher

    if lower_val > higher:
        return None 
    elif lower_val in values_sorted_array:
        return (higher, lower_val)
    else:
        next_higher_index = values_sorted_array.index(higher) + 1
        if len(values_sorted_array) > next_higher_index:
            next_higher = values_sorted_array[next_higher_index]
            return get_pair(next_higher)
        else:
            return None
    

def get_last_index(list, value):
    last_index = len(list) - list[::-1].index(value) - 1
    return last_index


def get_indexes(higher, lower):
    higher_index = values.index(higher)
    lower_index = -1
    if higher == lower:
        lower_index = get_last_index(values, lower)
        if higher_index == lower_index:
            return None
    else:
        lower_index = values.index(lower)
    
    return (higher_index, lower_index)


pair = get_pair()
msg = "IMPOSSIBLE"
if pair:
    higher, lower = pair
    indexes = get_indexes(higher, lower)
    if indexes:
        higher_index, lower_index = indexes
        msg = f"{higher_index + 1} {lower_index + 1}"
    
print(msg)