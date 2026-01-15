a = int(input("Enter a number between 1 and 10: "))

match a:
    case 1:
        print("You won mouse")
    case 3:
        print("you won nothing")
    case 8: 
        print("8$?")
    case _:
        print("Better luck next time")
        