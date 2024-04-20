# Sum of Two Values
# Input:

# 4 8
# 2 7 5 1
# Output:
# 2 4


_, total = map(int, input().split())
values = list(map(int, input().split()))
values_list = sorted(values, reverse=True)
top_value = -1
bottom_value = -1

index = 0
while index < len(values_list):
    if values_list[index] <= total:
        top_value = values_list[index]
        bottom_value_needed = total - top_value

        if bottom_value_needed > top_value:
            break

        try :
            index_bottom_value_needed = values_list.index(bottom_value_needed, index)
            if index_bottom_value_needed:
                bottom_value = bottom_value_needed
                break
        except ValueError :
            pass

    index += 1

if bottom_value != -1:
    top_value_index = values.index(top_value) + 1
    bottom_value_index = values.index(bottom_value) + 1
    print(f'{top_value_index} {bottom_value_index}')
else:
    print('IMPOSSIBLE')
