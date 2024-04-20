# Sum of Two Values
# Input:

# 4 8
# 2 7 5 1 5 7 3
# Output:
# 2 4




from array import array

# _, total = map(int, input().split())
# values = list(map(int, input().split()))

total = 3
values = values = list(map(int, "2 1 3".split()))
values_array = array('i', set(values))
values_sorted_array = sorted(values_array, reverse=True)

# get higher value
def get_higher_val(list_nums, total, higher_val):
    index = list_nums.index(higher_val)
    shorter_list_nums = list_nums[index:]
    for item in shorter_list_nums:
        if total - item >= 0:
            return item

# we find the lower value
def get_lower_val(list_nums, total, higher):
    lower = total - higher
    if lower in list_nums:
        return lower
    return None

# get both higher and lower values
def get_values(list_nums, total, higher=None):
    higher_val = get_higher_val(list_nums, total, higher_val)
    lower_val = get_lower_val(list_nums, total, higher_val)
    if lower_val:
        return (higher_val, lower_val)
    
    return None


# we get the indexes of the two numbers
def get_indexes(list_nums_original):
    values = get_values(values_sorted_array, total)
    if values:
        higher_val, lower_val = values
        higher_index = list_nums_original.index(higher_val)
        list_nums_original[higher_index] = -1
        if lower_val in list_nums_original:
            lower_index = list_nums_original.index(lower_val)
            return (higher_index, lower_index)
    
    return None


indexes = get_indexes(values)
if indexes:
    higher_index, lower_index = indexes
    print(f"{higher_index} {lower_index}")
else:
    print('iMPOSSIBLE')


""" 
12 8
2 7 5 1 5 7 3 10 9 6 8 9



-resolver que pasa si tengo el caso de que el TOTAL debo dividirlo a la mitad,
ejemplo TOTAL = 8 y values = [1, 2, 4, 4]
-
"""