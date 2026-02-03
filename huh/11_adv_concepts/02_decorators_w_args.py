
def repeat(n):
    def decorator(func):
        def wrapper(a):
            for i in range(n):
                func(a)
        return wrapper
    return decorator

@repeat(7)
def huh(a):
    print(f"hello!!! {a}")

huh("Rikin")