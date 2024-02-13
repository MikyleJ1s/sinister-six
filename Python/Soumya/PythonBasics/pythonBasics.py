# Print Statements ...

name = "Mikyle"
print("My name is " + name)

age = 23
print("I am", age, "yrs old")

# Memory Locations ...

a = 10
print(id(a)) 

print(id(20) == id(20))
b = 10
print(id(a) == id(b))
b = a
print(id(a) == id(b))

# Operators ...

print("Test %f" % 34)

# Type Conversion ...

print(int(3.3))
print(float(3))
print(int("7"))
print(str(2))

import math 
# Functions ...

def circleArea(radius):
    return math.pi * radius * radius

print(circleArea(7), " & ", circleArea(10))
    
# Inputs ... 
   
stop = 1    
k = 1
while k <6:
 
    if k > stop:
        stop+=1
        k = 1
        print()
    else: 
        print(k, end=' ')
        k+=1  

print()

for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end=' ')
    print()

country = "SouthAfrica"
print(country[1:3]) 
print(country[:5])
print(country[5:]) 
print(country[-1]) 
print(country[-4:-1]) 
print(country[::-1]) 

list1 = [1,2,"Bob", 3.5, True] # mutable because you can duplicate and change data in the list
print(list1[1:4:2]) # start, stop and step
print(list1)
list1.append("Mark")
list1[1:3] = [4, "Bobby"]
list1.remove(3.5)
print(list1)

tuple1 = (1,2,{'a','b', 'c'}, {8.3, "Tom"}) # immutable (this is for things like weekdays, month, dates or anything predefined)
print(tuple1)

set1 = {3,5, 5, 5, 5, 5,8,"John", 5.5} # duplicate values get ignored and everything gets reordered
print(set1)

dictionary1 = {1:"Mon", 2:"Tue", 3:"Wed", 1:"Meh"} # data structor that stores key values
print(dictionary1)



listSample = [10,1,3,5,4,6,8,7,2,9]

def multiplyList(listSample):
    answer = listSample[0]
    for i in range(1,len(listSample)):
        answer *= listSample[i]
    return answer

print(multiplyList(listSample))

print(max(listSample))


givenList = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
givenList.sort(key = lambda x: x[-1])
print(givenList)

# another way ...
def LastItem(input):
    return input[-1]

def sort(list_unsorted):
    return sorted(list_unsorted, key=LastItem)
print(sort(givenList))


from collections import Counter;
# how to create the counter# 
# 1) with sequence of items
print(Counter(['b','b','a','a'])) # with sequence of items
# with dictionary create counter
print(Counter({'a':3,'b':5,'c':2}))
# with arguments
print(Counter(a=3,b=2,c=1))
c = Counter()
c.update([1,2,2,2,2,2,3,3,3,3, 4,4])
print(c)

population = Counter({'South Africa': 59.39, "India": 1408.0, 'America': 331.9, 'Europe': 746.4, 'Australia': 25.69})
print(population.most_common(1))
print(population.total())


from collections import OrderedDict
print("This is data from the in-built dictionary: ")

d = {}
d['a'] = 1
d['b'] = 2 
d['c'] = 3
d['d'] = 4
for key, value in d.items():
    print(key, value)
print("This is data from the ordered dictionary: ")
 
oD = OrderedDict()
oD['a'] = 1
oD['b'] = 2 
oD['c'] = 3
oD['d'] = 4

for key, value in oD.items():
    print(key, value)

oD.pop('a')

print("After removing a: ")
for key, value in oD.items():
    print(key, value)
    
oD['a'] = 1

print("After reinserting back a: ")
for key, value in oD.items():
    print(key, value)
    


from collections import Counter
words = Counter()
words.update(input("Enter some words: ").split(' '))
print(words.most_common(10))


from collections import ChainMap
d1 = {'a': 1, 'b': 2}
d2 = {'b': 3, 'd': 4}
cM = ChainMap(d1,d2)
print(cM)
print(cM['b'])

from collections import namedtuple
Student = namedtuple('Student', ['name', 'age', 'DOB'])
S = Student('John', '19', '12062003')
print("The student age is: ", S[1])
print("The student age is: ", S.age)


from collections import deque
d1 = deque(['name', 'age', 'DOB'])
d1.append(4)
d1.appendleft(1)
print(d1)
d1.pop()
print(d1)
d1.popleft()
print(d1)

from collections import deque
d = deque([2,4,6,8,10,1,3,5,7,9])
print("Original deck: ", d)
n = int(input("Enter a number: "))
if n%2 == 0:
    d.appendleft(n)
else: 
    d.append(n)
print("After adding the number to the deck: ", d)


from collections import UserString
class MyString (UserString): # UserString is a parent
    def append(self, s):
        self.data += s
    def remove(self, s):
        self.data = self.data.replace(s, "")
s1 = MyString("John")
print("Original String: ", s1.data)

s1.append("s")
print("String After Appending: ", s1.data)

s1.remove("o")
print("String After Removing: ", s1.data)


input_list = [1,2,3,4,4,5,6,7,7]
dict_comp = {}
dict_comp = [i**3 for i in input_list if i%2!=0]
print(dict_comp)


state = ['Gujarat', 'Maharashtra', 'Rajasthan']
capital = ['Gandhinagar', 'Mumbai', 'Jaipur']

dict_comp = {state[i]:capital[i] for i in range(len(state))}
print(dict_comp)

dict_comp = {i: j for i, j in zip(state, capital)}
print(dict_comp)

input_list = [1,2,3,4,4,5,6,7,7]
set_comp = {i for i in input_list if i%2==0}
print(set_comp)

gen_comp = (i for i in input_list if i%2==0)
for i in gen_comp:
    print(i, end= " ")
#generators don’t allocate memory for the whole list.
'''
'''
from collections import UserString

class MyString (UserString): 

    alphabet = "abcdefghijklmnopqrstuvwxyz"
    
    def encrypt(self, message, e):
        self.data = ""
        for i in message:
            if i in self.alphabet:
                self.data += self.alphabet[(self.alphabet.index(i.lower()) + e)%26]
            else: 
                self.data += i

    def decrypt(self, message, d):
        self.data = ""
        for i in message:
            if i in self.alphabet:
                self.data += self.alphabet[(self.alphabet.index(i.lower()) - d)%26]
            else: 
                self.data += i

s1 = MyString(input("Original message:\t"))

e = int(input("\nEncryption integer:\t"))
s1.encrypt(s1.data, e)

print("After Encryption:\t",s1.data)

d = int(input("\nDecryption integer:\t"))
s1.decrypt(s1.data, d)

print("After Decryption:\t", s1.data)
'''
'''
password = input("Enter your password: ")
def validation(password):

    error = "Authentication successful."          

    if not any(char.islower() for char in password ):
        error = "Error: You need at least one lowercase letter."

    if not any(char.isdigit() for char in password):   
        error = "Error: You need at least one number."

    if not any(char.isupper() for char in password):
        error = "Error: You need at least one capital letter."

    if not any(char in "$#@" for char in password):
        error = "Error: You need at least one special character."
        
    if (len(password) < 6) or (len(password) > 12):
        error = "Error: You need a password of minimum length 6 and maximum length 12."

    return error

print(validation(password))

age = 0
try: 
    x = 10/age
except: 
    print(ZeroDivisionError)

a = [2,3,4,5]
try: 
    x = a[4]
    print(x)
except:
    print("Error occured")
else: 
    print("All good, no issues")
finally: 
    print("Finally")
print("Done with everything")


class InvalidAgeException(Exception):
    pass
number=28
try: 
    input_num=int(input("Enter the age:")) 
    if (input_num<=22 or input_num>=number):
        raise InvalidAgeException 
    else:
        print("Eligible")
except InvalidAgeException: 
    print("Exception occured: invalid age, not eligible")

class InvalidCredentials(Exception):
    pass
password = "hello5"
user = "bob"
try: 
    inputUser=input("User name: ")
    inputPassword = input("User password: ") 
    if (inputUser!=user or inputPassword!=password):
        raise InvalidCredentials 
    else:
        print("Verified")
except InvalidCredentials: 
    print("Exception occured: invalid user or password")

class FahrenheitError(Exception):
    pass

def fahrenheit_to_celsius(temperature):
    return (temperature - 32)*5/9
    
try: 
    temperature=float(input("Temperature: ")) 
    if (temperature<32 or temperature>212):
        raise FahrenheitError 
    else:
        print(fahrenheit_to_celsius(temperature))
except FahrenheitError: 
    print("Exception occured: Not a valid fahrenheit range")



class CustomError(Exception):
    pass

class LengthError(CustomError):
    pass
    
class TypeError(CustomError):
    pass
try: 
    number=input("Mobile Number: ") 
    if (len(number) == 10): 
        try: 
            for digit in number: 
                if int(digit) in range(0,10):
                    pass
            print("Valid Number")
        except:
            raise TypeError
    else: 
        raise LengthError
except CustomError: 
    print("Invalid Number")



def shout(text):
    return text.upper()
def whisper(text):
    return text.lower()
def greet(func):
    greeting = func("Hello There")
    print(greeting)
    
greet(shout)
greet(whisper)

yell = shout
print(yell("i am shouting"))

def createAdd(x):
    def add(y):
        return x+y
    return add

addx = createAdd(15)
print(addx(10))


def cube(x):
    return x**3

def myMap(method, alist):
    result = list()
    for item in alist:
        result.append(method(item))
    return result

alist = myMap(cube, [1,2,3,4,5])
print(alist)

from datetime import date, time

def createLogger(message):
    def log():
        print("Log Message: "+message+ " "+str(date.today()))
    return log

log1 = createLogger("Hello")
log2 = createLogger("World")
log1()
log2()
'''

class CustomError(Exception):
    pass

class ItemError(CustomError):
    pass

class QuantityError(CustomError):
    pass

store = {"rice":0, "oil":3, "sugar":1, "fish":5, "meat":2}

choice = input("Which item would you like to buy: ")
try: 
    if choice.lower() in store:
        if store[choice.lower()] < 1:
            raise QuantityError
        print("Item you bought: "+choice)
    else:
        raise ItemError
except CustomError: 
    print("Item is not available at this store")
    
class itemNotInStoreException(Exception):
    pass
class invalidQtyException(Exception):
    pass
Stock = {"rice":2, "oil":4, "sugar":1,"fish":0,"meat":10}
print("Our stock items: ", Stock.items())
    
def validate(item ,qty):
    for i,q in Stock.items():
        if(i == item and qty<=q):
            Stock.update({i:q-qty})
            return q
        else:
            return -1
while True:
    item = input("Enter an item to purchase: ")
    qty = int(input("Enter quantity: "))
    try:
        if(qty<0):
            raise invalidQtyException
        elif(validate(item,qty)==-1):
            raise itemNotInStoreException
    except invalidQtyException:
        print("invalid qty entered") 
    except itemNotInStoreException:
        print("Item not in store")
    else:
        print("Item purchased")
        print("Updated stock list: ", Stock.items())
        break
'''

import hello
hello.message("Hello")

import os
path = "C:/"
directoryList = os.listdir(path)
print(directoryList)
print(os.getcwd())
directory = "testfolder"
parentDirectory = "C:/"
path = os.path.join(parentDirectory, directory)
print(path)
#os.mkdir(path)


    
file = open("sample.txt", "w")
file.write("Hello\n")
file.close()
try:
    f = open("sample.txt", 'r')
    text = f.read()
    f.close()
    #os.rename("sample.txt", "filename.txt")
    #os.remove("sample.txt")
    #print(os.path.exists("sample.txt"))
    #print(os.path.getsize("sample.txt"))
except IOError as e:
    print(e)

import datetime
year = int(input('Input year: '))
month = int(input('Input month: '))
day = int(input('Input day: '))
date1 = datetime.date (year, month, day)
curr = date1
lst = []
lst.append(curr)
for _ in range(12):
    lst.append(curr + datetime.timedelta(days=20))
    curr+=datetime.timedelta(days=20)
    for i in range(len(lst)):
        date = lst[i].strftime('%m/%d/%Y')
        print("date: %s" % date)

from datetime import date, datetime, timedelta
myDate = date(1999, 2, 21)
print(myDate)
print(date.today())   
print(date.today().year - myDate.year)   
print(datetime.fromtimestamp(10000000000))
print(type(datetime.isoformat(datetime.today())))



myDate = date(2022,2,28)
for i in range(0,11):
    print(myDate+ timedelta(days=20))
    myDate = myDate+ timedelta(days=20)


from datetime import *
'''
day = int(input("Day: "))
month = int(input("Month: "))
year = int(input("Year: "))  

print(datetime.isocalendar(date(year, month, day)).week)


from datetime import date, timedelta

def all_sundays(year):
# January 1st of the given year
       dt = date(year, 1, 1)
# First Sunday of the given year       
       dt += timedelta(days = 6 - dt.weekday())  
       while dt.year == year:
          yield dt
          dt += timedelta(days = 7)
year = int(input("Select all Sundays in Year: "))
for s in all_sundays(year):
   print(s)

import datetime
year = int(input("Enter year please: "))
date = datetime.date(year, 1, 1) 
while date.year == year: 
    if date.weekday() == 6: 
        print(date.isoformat()) 
    date += datetime.timedelta(days=1)

'''



from datetime import *
import pytz

southAfrica = pytz.timezone("Africa/Johannesburg")
india = pytz.timezone("Asia/Kolkata")
saTime = datetime.now(southAfrica).strftime("%H:%M:%S")
iTime = datetime.now(india).strftime("%H:%M:%S")
print("South Africa: ", saTime)
print("India: ", iTime)

import datetime
tday=datetime.date(2017,6,18)
bday=datetime.date(2017,9,18)
till_bday=bday-tday
print(till_bday)


from functools import reduce


def cube(y):
    return y**3

lambdaCube = lambda y : y**3

print("Using the function: ",cube(3))
print("Using the lambda function: ",lambdaCube(3))

evenList = [lambda arg=x: arg*10 for x in range(1,5) ]
for item in evenList:
    print(item())
    
    
max = lambda a,b: a if a>b else b
print(max(4,1))


mylist = [[26,3,4], [1,22,35,4],[201,33,41,5,6]]

sortedList = lambda x: (sorted(i) for i in x)
secondLargest = lambda x, f: [y[len(y)-2] for y in f(x)]

result = secondLargest(mylist, sortedList)
print(result)

mylist = [5,6,7,89, 56, 34, 67, 56]
evenList = list(filter(lambda x: (x%2==0), mylist))
print(evenList)
print(list(map(lambda x: x*2, mylist)))
print((reduce((lambda x,y: x+y), mylist)))

mylist = ["adam", "michael", "carl", "tom", "arnold", "bob", "ashley"]
print(list(filter(lambda x: x[0] == "a", mylist)))
print(list(map(lambda x: x.upper(), mylist)))

dictionary = [{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Mi Max', 'model': '2', 'color': 'Gold'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}]
dictionary.sort(key=lambda x: int(x['model']))
print(dictionary)

print(sorted(dictionary, key=lambda i: i['make']))

strings=['php', 'w3r', 'Python', 'abcd', 'Java', 'aaa']
print(list(filter(lambda x: x==x[::-1], strings)))

strings = [1, 'abcd', 3.12, 1.2, 4, 'xyz', 5, 'pqr', 7, -5, -12.22]
print(len(list(filter(lambda x: (type(x) == float), strings))))

tuples = ((10, 10, 10), (30, 45, 56), (81, 80, 39), (1, 2, 3))
print(tuple(map(lambda x: sum(x)/float(len(x)), zip(*tuples))))

listwords = ['orange', 'red', 'green', 'blue', 'white', 'black']
removewords = ['orange', 'black']
print(list(filter(lambda x: (x not in removewords), listwords)))


from functools import reduce
import re
s = "i am learning python regEx. right now"
match = re.search("learning", s)
print("Start Index: ", match.start())
print("Ending Index: ", match.end())

match = re.search(r'.', s) # match with first character
print(match)

match = re.search(r'\.', s)
print(match)

match = re.search(r'[py]', s)
print(match)

match = re.search(r'[^py]', s)
print(match)


s = "my phone number is 0849014837 so call me, i am 23"
match = re.findall('\d+', s)
print(match)

p = re.compile('[a-e]')
print(p.findall("Hello there, said Mikyle"))
p = re.compile('[^a-e]')
print(p.findall("Hello there, said Mikyle"))
p = re.compile('\w') # a to z, A to z or 9 to 0
print(p.findall("Hello there, said Mikyle"))
p = re.compile('\w+') # a to z, A to z or 9 to 0
print(p.findall("Hello there, said Mikyle"))

s = "this is aBsolutely GrEat"

print(re.search(r'[a0]|[A0]|[AB*]|[Ab*]|[\s]', s))

print(re.search('[A-Z]+[a-z]+$', s))

s = "Exercises number 1, 12, 13, 354, 4564 are important"
print(re.findall('[0-9]{1,3}', s))


from functools import reduce
from re import split
import re
print(split('\w+', "i am learning = python")) # non alphanumeric
print(split('\W+', 'i am learning = python'))
print(split('\d+', 'on 15th of feb 2023 at 10:02 am'))

s = "I have 22 apples and 14 bananas 34 mangos"
numbers = (re.findall('\d+', s))

print(numbers)

numbers = [int(i) for i in numbers]

print((reduce((lambda x,y: x+y), numbers)))

s = 'Wrong Road'
print(re.sub('Road', 'Rd.', s))

import re
try: 
    f = open("filename.txt", 'r')
    text = f.read()
    f.close()
    print(re.findall('\w+@\w+.\w+', text))
except IOError as e:
    print(e)
    
# higher order function
def adding(a):
    def addition(b):
        return a+b
    return addition

a = int(input("a: "))
b = int(input("b: "))
addvariable = adding(a)
result = addvariable(b)
print("a + b =", result)


file = open("sample.txt", 'r')
#print(file.read())
#print(file.read(2))
#print(file.readline())
#print(file.readline(2))
#print(file.readlines())

file = open("sample.txt", 'a')
file.write("Jones\n")
file.close()
file = open("sample.txt", 'r')
print(file.read())
file.close()
file = open("sample.txt", 'w')
file.write("I AM TAKING OVER\n")
file.close()
file = open("sample.txt", 'r')
print(file.read())
file.close()

with open("sample.txt", 'r') as file:
    file.seek(4)
    data = file.readlines()
    for line in data:
        word = line.split()
        print(word)
        print(file.tell())

import csv 
    
heading = ['Name', 'Surname', 'Age'] 

info = [ ['Joe', 'Smo', '35'],  
         ['Kid', 'Bob', '18']] 

with open('csvfile.csv', 'w') as file: 
    csvwriter = csv.writer(file) 
    csvwriter.writerow(heading) 
    csvwriter.writerows(info)

with open('csvfile.csv', 'r') as file:
    for line in file.readlines():
        print(line)


f = open('photo.jpg', 'rb')
print(f.read())

f = open('demo.bin', 'wb')
a = [100,12,12]
arr = bytearray(a)
print(arr)
f.write(arr)
f.close()


count = 0
'''
try:
    filename = input("File Name: ")
    with open(filename,'r') as file:
        data = file.read()
        count += len(data.split())
        print(count)
except: 
    print("No Such File")
'''

    
    
import json 
with open("sample.json", 'r') as f:
    data = json.load(f)
print(data)

dict1 = {"name": "John", "age": 12}
print(type(dict1))
dict1_json = json.dumps(dict)
print(dict1_json)
print(type(dict1_json))