first_name = input("What is your name? ")

greeting = '''Hello {}
How are you doing?
I hope you have a great career.
Have a excellent day
'''

print(greeting.format(first_name))

print(f"This is my {first_name} name")