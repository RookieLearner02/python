car = input("Enter Car Name: ")

match car:
    case "ford":
        print("Your car is a Ford")
    
    case "chevy":
        print("Your car is a Chevy")
    
    case "toyota":
        print("Your car is a Toyota")
    
    case _:
        print(f"Your value is not a ford, chevy, or toyota")