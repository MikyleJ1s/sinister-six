from functools import reduce

def addition(x,y):
    return x+y

def subtraction(x,y):
    return x-y

def multiplication(x,y):
    return x*y

def linear_search(x,y):
    if x in y:
        return True
    return False

def binary_search(x, y):
    low = 0
    high = len(y) - 1
    middle = 0
    
    # in case it is not sorted ...
    y = sorted(y)
 
    while low <= high:
 
        middle = (high + low) // 2
        if x > y[middle]:
            low = middle + 1
 
        elif x < y[middle]:
            high = middle - 1

        else:
            return True
 
    return False

def substring_search(x, y):
    if y.find(x) in range(0, len(y)):
        return True
    return False

# Python Program for Find largest prime factor of a number
#pdb.set_trace() 

def is_prime(n): 
    for j in range(2, n): 
        if n % j == 0: 
            return False 
    return True 

def prime_factors(n): 
    my_list = [] 
    for i in range(2, n+1): 
    
        if n % i == 0 and i != n:  
            if is_prime(i): 
                my_list.append(i) 
        elif i == n and is_prime(i):
            my_list.append(i)

    if len(my_list) != 0:
        return my_list

def max_prime_factors(array):
    return max(array)

# Python Program for Efficient program to print all prime factors of a given number

# Python Program for Product of unique prime factors of a number
def product_prime_factors(n):
    return reduce((lambda x,y: x*y), prime_factors(n))

# Python Program for Find sum of odd factors of a number
def sum_odd_factors(n): 
    my_list = 0
    for i in range(1, n+1): 
        if n % i == 0 and i%2 !=0:  
            my_list += i 

    return my_list

# Python Program for Coin Change



