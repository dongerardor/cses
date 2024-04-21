""" 
Input:

4 3 5
60 45 80 60
30 60 75

Output:
2

"""

applicants_qty, apartments_qty, diff = map(int, input().split())
applicants = sorted(list(map(int, input().split())))
apartments = sorted(list(map(int, input().split())))

i = 0 # applicants cursor
j = 0 # apartments cursor
sold = 0
while i < len(applicants) and j < len(apartments):
    is_bigger = apartments[j] > applicants[i] + diff
    is_smaller = apartments[j] < applicants[i] - diff

    if is_bigger:
        i += 1
    elif is_smaller:
        j += 1
    else:
        i += 1
        j += 1
        sold += 1
    
print(sold)
