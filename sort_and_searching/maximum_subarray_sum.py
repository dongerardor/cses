"""

Input:
8
-1 3 -2 5 3 -5 2 2
Output:
9

"""

# length = int(input())
# values = list(map(int, input().split()))

def have_different_signs(a, b):
    return (a * b) <= 0

length = 15
#values = [-8, -1, 3, -2]
values = [-1, 3, -2, 5, 3, -5, 2, 2, -2, -1, 5, 9, -8, -7, 3]

condensed_values = []
subarr = []

i = 0
is_prev_positive = False
acc = 0

while i < len(values):
    prev_val = values[i - 1] if i > 0 else -1
    val = values[i]
    if have_different_signs(prev_val, val) and len(subarr):
        condensed_values.append(sum(subarr))
        subarr = []
                
    subarr.append(val)
    i += 1
else:
    condensed_values.append(sum(subarr))

if condensed_values[0] < 0:
    condensed_values[0] = 0


j = 0
condensed_condensed_values = []
while j < len(condensed_values):
    val = condensed_values[j] + condensed_values[j + 1]
    condensed_condensed_values.append(val)
    j += 2



k = 0
subarr2 = []
result_arr = []

while k < len(condensed_condensed_values):
    prev_val = values[k - 1] if k > 0 else 0
    val = values[k]
    if have_different_signs(prev_val, val):
            condensed_values.append(sum(subarr))
            subarr = []




# como sumar los numeros positivos contiguos y los numeros negativos contiguos
# de forma que me queden numeros unicos positivos alternados con numeros unicos negativos?


""" 


    if values[i] < 0 and len(subarr):
        condensed_values.append(subarr)
        subarr = []
    subarr.append(values[i])
    i += 1
else:
    condensed_values.append(subarr)


for i, val in enumerate(values):
    prev_val = values[i - 1] if i > 0 else 0

    is_not_empty = len(subarr) > 0
    is_break = prev_val >= 0 and val < 0
    is_ending = i == len(values) - 1
    if is_not_empty and (is_break or is_ending):
        condensed_values.append(subarr)
        subarr = []
    subarr.append(val)


"""