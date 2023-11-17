
try:
    number = input("(100/number) Enter a Number: ")

    value = 100 / int(number)

    print(value)

except ValueError:
    print("Please Enter a Numerical value")

except ZeroDivisionError as exc:
    print(exc)
    print("Number Cannot Be 0(Zero)")

print("Appreciate Your Input.")