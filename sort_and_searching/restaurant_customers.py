n = int(input())

cust_stay_input = []
cust_stay = []
count = n
while count > 0:
    count -= 1
    cust_stay_input.append(input())

for str in cust_stay_input:
    ab = (int(str[0]), int(str[2]))
    cust_stay.append(ab)
    
def diff(tupl):
    return abs(tupl[0] - tupl[1])

cust_stay_ordered = sorted(cust_stay, reverse=True, key=diff)

counter = 0
