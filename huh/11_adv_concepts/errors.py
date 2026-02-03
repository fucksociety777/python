while True:
    try:
        a = int(input("Enter number 1: "))
        b = int(input("Enter number 2: "))
        # print(f"The sum is {a + b}")
        print(f"Th division is {a/b}")
        
    except ValueError:
        print("Please dont perform bad typecasts")

    except ZeroDivisionError:
        print("Hey dont divide by 0")
        
    except Exception as e:
        print("Enter number only !!", e)
        
