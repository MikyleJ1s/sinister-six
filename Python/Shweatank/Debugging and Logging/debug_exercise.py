from functools import reduce
import sys, logging, pdb

'''
# initial example ...

#print(sys.argv[1])

if len(sys.argv) == 1:
    name = sys.argv[1]

else:
    name = 'stranger'

print(f'Hi there, {name}')

'''

# function to do all the operations ...
def calculate(x,y,z):
    
    # addition ...
    if z == '+':
        print(x,"+",y,"=",x+y)
    
    # subtraction ...
    elif z == '-':
        print(x,"-",y,"=",x-y)
        
    # multiplication ...
    elif z == '*':
        print(x,"*",y,"=",x*y)
        
    # division ...
    elif z == '/':
        if y!=0:
            print(x,"/",y,"=",x/y)
        else:
            print("Can't divide by zero!")

# check if all arguments are given ...
if len(sys.argv) > 1:
    
    # get the arguments ...
    x = int(sys.argv[4]) 
    y = int(sys.argv[5])
    
    # now get the operator ... 
    z = sys.argv[6]
    
    # do the calculation ...
    #pdb.set_trace()
    calculate(x,y,z)

# in the launch.json file:
# "args": ["1","5", "/"] 

# Python Program for n\’th multiple of a number in Fibonacci Series
def fibonacci(x):
    if x < 0:
        return "Invalid"
    elif x == 0:
        return 0
    elif x == 1 or x == 2:
        return 1
    return fibonacci(x-1) + fibonacci(x-2)

n = int(sys.argv[1])
print("Fibonacci of", n,": ", fibonacci(n))

# Program to print ASCII Value of a character
n = sys.argv[2]
print("Ascii Value of", n, ": ", ord(n))

# Python Program for Sum of squares of first n natural numbers
def squares(n):
    answer = 0
    for i in range(1,n+1):
        answer = answer + (i*i)
    return answer
        
n = int(sys.argv[1])
print("Sum of Squares of the First", n, "Natural Numbers: ", squares(n))

# Python Program for cube sum of first n natural numbers
def cube(n):
    answer = 0
    for i in range(1,n+1):
        answer = answer + (i**3)
    return answer

n = int(sys.argv[1])
print("The Sum of Cubes of the First", n, "Natural Numbers: ", cube(n)) 

# Python | Cloning or Copying a list
original = list((sys.argv[3]).split(','))
duplicate = (original.copy())
print("Original List: ", original, "Copied List: ", duplicate)

# Python | Count occurrences of an element in a list
n = int(sys.argv[1])
print("Number of Times", n, "Appears in the List: ", original.count(str(n)))

# Python | Remove empty tuples from a list

# Python | Program to print duplicates from a list of integers
def removeduplicates(original):
    duplicates = []
    uniques = []
    
    for i in original:
        if i not in uniques:
            uniques.append(i)
        else:
            duplicates.append(i)
    return duplicates

print("Duplicates: ", removeduplicates(original))

logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger()
logger.setLevel(logging.INFO)
logger.debug("Debug Message")
logger.info("Info Message")
logger.warning("Warning Message")
logger.error("Error Message")
logger.critical("Critical Message")

# Python Program to Reverse a linked list

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

n = int(sys.argv[1])
print("Largest Prime Factor of",n,": ",max(prime_factors(n))) 

def max_prime_factors(array):
    return max(array)

# Python Program for Efficient program to print all prime factors of a given number
print("All Prime Factors of",n,": ",(prime_factors(n))) 

# Python Program for Product of unique prime factors of a number

factors = reduce((lambda x,y: x*y), prime_factors(n))
print("Product of the Prime Factors of",n,": ",factors)

# Python Program for Find sum of odd factors of a number
def odd_factors(n): 
    my_list = 0
    for i in range(1, n+1): 
        if n % i == 0:  
            my_list += i 

    return my_list
print("Sum of the Odd Factors of",n,": ",odd_factors(n))
# Python Program for Coin Change

