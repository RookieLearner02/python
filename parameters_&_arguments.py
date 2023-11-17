"""

Parmeters --  is a variable that store information so function can perform its job

Arguments -- is also a variable that store information but it is passed when calling a function

"""

def greet_the_user(name):
    
    """

    Args:
        name (str): this function collects the user Full name
    
    """

    print(f"\t Hello {name}, how are you?")
    print("\t this is a python programming class")


greet_the_user(input("Please enter Your Full name?"))