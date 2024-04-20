# target = 3
# values = list(map(int, "1 1 1 1 1 1 1 1 1 1 1 1 1".split()))
# 4 8
# 2 7 5 1
# target = 8
# target = 3
# input_values = list(map(int, "1 1 1 1 1 1 1 1 1 1 1 1 1".split()))


from array import array
from copy import copy

_, target = map(int, input().split())
input_values = list(map(int, input().split()))
values = sorted(array('i', set(input_values)), reverse=True)

def find_pair(_list, target):
    cursor_high = 0
    cursor_low = len(_list) - 1
    
    while cursor_high < cursor_low:
        high = _list[cursor_high]
        low = _list[cursor_low]
        _sum = high + low
        if target < _sum:
            cursor_high += 1
        elif target > _sum:
            cursor_low -= 1
        else:
            return (high, low)
        
def check_half_values(_list, target):
    half = target // 2 if target % 2 == 0 else None
    if half in _list:
        cursor_high = _list.index(half)
        _list[cursor_high] = -1
        if half in _list:
            cursor_low = _list.index(half)
            if cursor_low:
                return (cursor_high, cursor_low)

    return None 

pair = find_pair(values, target)

if pair:
    high, low = pair
    index_high = input_values.index(high)
    index_low = input_values.index(low)
    print(f"{index_high + 1} {index_low + 1}")
else:    
    half_values_indexes = check_half_values(input_values, target)
    if half_values_indexes:
        index_high, index_low = half_values_indexes
        print(f"{index_high + 1} {index_low + 1}")
    else:    
        print("IMPOSSIBLE")








""" 
pair = find_pair(values, target)
if pair:
    index_high, index_low = pair
    print(f"{index_high + 1} {index_low + 1}")
else:
    half_values_indexes = check_half_values(input_values, target)
    if half_values_indexes:
        index_high, index_low = half_values_indexes
        print(f"{index_high + 1} {index_low + 1}")
    else:    
        print("IMPOSSIBLE")


"""