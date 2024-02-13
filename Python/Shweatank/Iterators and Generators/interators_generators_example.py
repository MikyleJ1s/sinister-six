my_order = ["Castle Lite", "Heineken", "Coca Cola"]
for item in my_order:
    print(item)
lowered = [item.lower() for item in my_order]

ranked_chocolate = ("Dark", "Milk", "White")
for chocolate in ranked_chocolate:
    print(chocolate)
    
prices = {"pineapple": 9.99, "pen": 2.99, "pineapple-pen": 19.99}
for product in prices:
    print(product, "costs", prices[product])
discounted = {item: prices[item] * 0.75 for item in prices}

best_topping = "pineapple"
for letter in best_topping:
    print(letter)

x = list(prices.keys())[0]
for i in prices:
    if prices[x] > prices[i]:
        x = i
        
print("Min: ", prices[x])

numbers = ["one", "two", "three", "four"]

numberator = iter(numbers)
print(next(numberator))
print(next(numberator))
print(next(numberator))
print(next(numberator))

try: 
    print(next(numberator))
except:
    print("You have reached the end")

chocolatator = iter(ranked_chocolate)
try:
    while True:
        print(next(chocolatator))
        
except:
    print("You have reached the end")
    
def get_even():
    n = 0
    while n < 10:
        yield n
        n = n + 2
        
obj = get_even()
print((next(obj)))
print((next(obj)))
print((next(obj)))

def evens(start, end):
    num = start + (start%2)
    while num < end:
        yield num 
        num += 2
        
for num in evens(12,60):
    print(num)

def fibonacci(n):
    x, y = 0, 1
    for i in range(n):
        yield x
        x, y = y, x + y

print(list(fibonacci(2)))

# Write a Python program to find the factorial of a number using itertools module.

# Write a Python program to make an iterator that drops elements from the iterable as soon as an element is a positive number
def is_positive(array):
    for i in array:
        yield i
            
            
obj = is_positive([-1,-2,-3,4,-10,2,0,5,12])
try:
    while True:
        if next(obj) > 0:
            print(next(obj), end=" ")
except:
    print("Done") 
# Write a Python program to construct an infinite iterator that returns evenly spaced values starting with a specified number and step

def hello_decorator(func):

    def inner1(*args, **kwargs):

        print("before Execution")
        
        # getting the returned value

        returned_value = func(*args, **kwargs)

        print("after Execution")

        # returning the value to the original frame

        return returned_value

    return inner1

# adding decorator to the function

@hello_decorator

def sum_two_numbers(a, b):

    print("Inside the function")

    return a + b 

a, b = 1, 2 # getting the value through return of the function

print("Sum =", sum_two_numbers(a, b))