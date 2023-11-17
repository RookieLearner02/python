'''
Default value -- it is a backup value / default value if the the
                 arguments is not mentioned while calling the function.
'''
welcome_the_user()

def welcome_the_user(name = 'John Doe', age = '25'):
    """

    Args:
        name (str, optional): This is the Full name of the user. Defaults to 'John Doe'.
        age (str, optional): This is a age of the user. Defaults to '25'.
    """

    print(f"\t Hello {name}, Welcome to the python program \n")
    print(f" \tYou have mentioned your age as, {age} years old. \n")

    if int(age) >= 18:
        print("\t You are not eligible for any discounts. \n")
    else:
        print("\t You got $50 discount on the total price. \n")


print("Welcome to the course. \n")

# welcome_the_user(input("Please enter user full name :"), 
#                  input("Please mention  your age: "))

print("Thanks for attending the python course. \n")