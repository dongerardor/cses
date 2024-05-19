length = 15
#values = [-8, -1, 3, -2]
values = [-1, 3, -2, 5, 3, -5, 2, 2, -2, -1, 5, 9, -8, -7, 3]

max_subarray_sum = 0
subarray_sum = 0
i = 0

while i < len(values):
    subarray_sum = max(subarray_sum, subarray_sum + values[i])
    if max_subarray_sum < subarray_sum:
        max_subarray_sum = subarray_sum
    i += 1

print(max_subarray_sum)