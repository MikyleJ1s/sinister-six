def increment(x):
    return x + 1

def decrement(x):
    return x - 1

def add(a,b):
    return a + b

def factorial(x):
    if x < 0:
        return "Does not exist"
    elif x == 0 or x == 1:
        return 1
    return x * factorial(x-1)

def fibonacci(x):
    if x < 0:
        return "Invalid"
    elif x == 0:
        return 0
    elif x == 1 or x == 2:
        return 1
    return fibonacci(x-1) + fibonacci(x-2)