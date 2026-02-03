# Decorator is a function that takes a function, it creates a new function inside its body (wrapper). Then it returns that new function
def decorator(func):
    def wrapper():
        print("I am about to execute a function....")
        func()
        print("I have executed this function....")
    return wrapper
@decorator
def huh():
    print("HUHUHUH")
    
huh()
    
# f = decorator(huh)
# f()

'''
f will look something like this
def f():
     print("I am about to execute a function....")
     print("HUHUHUH")
     print("I have executed this function....")

'''
