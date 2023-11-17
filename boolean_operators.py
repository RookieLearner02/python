#  Boolean Operators

"""

Identity 

| Operator | Name                                           |
| is       | Returns True if the objects are the same       |
| is not   | Returns True if the objects are not the same   |


Membership

| Operator  | Name                                                      |
| in        | Returns True if a value is specified in a sequence        |
| not in    | Returns True if a value is not specified in a sequence    |

"""


# Identity Operators

address_34 = ["red", "black", "white"]

address_38 = ["red", "black", "white"]

print(address_34 is address_38)

print(id(address_38))
print(id(address_34))

print(address_34 is not address_38)

address_34 = address_38

print(id(address_38))
print(id(address_34))

print(id(address_34) is id(address_38))

# Membership operators

message = "I like Programming In Python"

print("Python" in message)

print("programming" in message)

print("Like" not in message)