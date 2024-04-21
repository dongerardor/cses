"""  

Input:

5 3
5 3 7 8 5
4 8 3

Output:
3
8
-1

"""

tickets_qty, customers_qty = map(int, input().split())
ticket_prices = sorted(list(map(int, input().split())), reverse=True)
customer_prices = list(map(int, input().split()))

for customer_price in customer_prices:
    for i, ticket_price in enumerate(ticket_prices):
        if ticket_price and ticket_price <= customer_price:
            print(ticket_price)
            ticket_prices[i] = None
            break
    else:
        print(-1)