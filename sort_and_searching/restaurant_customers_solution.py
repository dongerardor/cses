def solucion(customers):
    arrival = sorted([i[0] for i in customers])
    departure = sorted([i[1] for i in customers])

    n = len(arrival)
    i = 0
    j = 0
    current_customers = 0
    max_customers = 0

    while i < n and j < n:
        if arrival[i] <= departure[j]:
            current_customers += 1
            i += 1
        else:
            j += 1
            current_customers -= 1
        max_customers = max(max_customers, current_customers)

    return max_customers

n = int(input())
customers = []
for _ in range(n):
    customer_in, customer_out = map(int, input().split())
    customers.append((customer_in, customer_out))
    
print(solucion(customers))
