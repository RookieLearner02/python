"""

if-else

"""


'''

if you are 18 old or older
    confirm you can Drive
    then get a licence

if not 18
    Sorry but you are not old enough to drive
    Plese come back when you are 18 or older

'''

age = int(input("What is your age? "))

if age >= 18:
    print("Answer the question below in yes or no")
    conformation = input("Can you Drive? ")
    if conformation.lower() == "yes":
        print("Collect you Licence")
    else:
        print("Learn to drive, and then collect your licence.")
else:
    print("sorry but you are not old enough.\nPlease come back when you're 18 or older")

print("Have a good day. Thank you")