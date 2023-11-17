'''

nested-if

'''


price = float(input("Plase enter bill amount $"))

if price > 0:
    if 0 <= price <= 99.99:
        print("You are not qualified for the discount.")
        discount = 0

    elif 100 <= price <= 199.99:
        discount = 10.00
    
    elif 200 <= price <= 299.99:
        discount = 25.00

    elif 300 <= price <= 399.99:
        discount = 50.00
    
    else:
        discount = 60.00
    print("Your Discount is $%.2f" % discount)
    total_price = price - discount
    print("Payable Bill is $%.2f " % total_price)
    # we can use $%.2f to round the floating point number to 2 decimal

else:
    print("Please enter positive number.")
