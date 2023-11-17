'''

if_elif_else

'''


"""

(1) if the price is >= $100 and <= $199.99
        then the customer gets a $10 Discount
(2) if the price is >= $200 and <= $299.99
        then the customer gets a $25 Discount
(3) if the price is >= $300 and <= $399.99
        then the customer gets a $50 Discount
(4) if the price is >= $400
        the the customer gets $60 Discount

"""

price = float(input("Please enter the total bill amount...  $"))

if price < 100:
    print("You have no discount.")
    print(f"You have to pay ${price}")

elif 100 <= price <= 199.99:
    disounted_total_amount = price - 10
    print("You got $10 Discount")
    print(f"You have to pay ${disounted_total_amount}")

elif price >= 200 and price <= 299.99:
    disounted_total_amount = price - 25
    print("You got $25 Discount")
    print(f"You have to pay ${disounted_total_amount}")

elif price >= 300 and price <= 399.99:
    disounted_total_amount = price - 50
    print("You got $50 Discount")
    print(f"You have to pay ${disounted_total_amount}")

else:
    disounted_total_amount = price - 60
    print("Tou got $60 Discount")
    print(f"You have to pay ${disounted_total_amount}")

print("Have a great day.  ")
