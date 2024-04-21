# n = int(input())
# customers = []
# for _ in range(n):
#     customer_in, customer_out = map(int, input().split())
#     customers.append((customer_in, customer_out))
# n = 5
# customers = [(5, 8), (2, 4), (3, 9), (5, 7), (4, 6)]

""" 


n = 4
customers = [(1, 10), (2, 4), (3, 5), (7, 9)]

##
n = 4
customers = [(1, 10), (2, 4), (3, 5), (7, 9)]
##

# n = int(input())
# customers = []
# for _ in range(n):
#     customer_in, customer_out = map(int, input().split())
#     customers.append((customer_in, customer_out))


n = 4
customers = [(1, 10), (2, 4), (3, 5), (7, 9)]


4
1 10
2 4
3 5
7 9


"""

n = int(input())
customers = []
for _ in range(n):
    customer_in, customer_out = map(int, input().split())
    customers.append((customer_in, customer_out))

def solucion(customers):
    entrances = sorted([i[0] for i in customers])
    leaves = sorted([i[1] for i in customers])

    cursor_entrances = 0
    cursor_leaves = 0
    people_present = 0
    max_amount_of_people = 0

    while cursor_entrances < n and cursor_leaves < n:
        entrance_time = entrances[cursor_entrances]
        leave_time = leaves[cursor_leaves]
        hour = min(entrance_time, leave_time)
        if entrance_time == hour:
            people_present += 1
            cursor_entrances += 1
        if leave_time == hour:
            people_present -= 1
            cursor_leaves += 1
            
        max_amount_of_people = max(people_present, max_amount_of_people)

    return max_amount_of_people


print(solucion(customers))