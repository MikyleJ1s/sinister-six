'''
1) Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
between 2000 and 3200 (both included).
The numbers obtained should be printed in a comma-separated sequence on a single
line.
'''
#print([i for i in range(2000, 3201) if (i % 7 == 0) & (i % 5 != 0)])

'''
2) Write a program which can compute the factorial of a given numbers.
The results should be printed in a comma-separated sequence on a single line.
'''
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n-1)

#print(factorial(3))

'''
3) Write a program to print
###**
###**
###**
**###
**###
'''
def pattern(a, b):
    for i in range(a):
        print("#" * a + "*" * b)
    for j in range(b):
        print("*" * b + "#" * a)

#pattern(3,2)
'''
4) Write a Python program to print a specified list after removing the 0th, 4th and 5th elements. 
Sample List : [Red, Green, White, Black, Pink, Yellow]
Expected Output : [Green, White, Black]
'''
sampleList = ["Red", "Green", "White", "Black", "Pink", "Yellow"]
outputList = [colour for (index, colour) in enumerate(sampleList) if index not in (0,4,5)]

#print(outputList)

'''
5) Write a program that accepts a sequence of whitespace separated words as input and prints the words after
removing all duplicate words and sorting them alphanumerically.
Suppose the following input is supplied to the program:
hello world and practice makes perfect and hello world again
Then, the output should be:
again and hello makes perfect practice world
Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
We use set container to remove duplicated data automatically and then use sorted() to sort the data.
'''


def remove():
    sentence = input("Write a sentence: ").split(' ')
    setContainer = {sentence[0]}
    for i in sentence:
        setContainer.add(i)
    setContainer = sorted(setContainer)
    print((' ').join(setContainer)) 

#remove()

'''
1) You are required to write a program to sort the (name, age, height) tuples by ascending order
where name is string, age and height are numbers. The tuples are input by console. The sort
criteria is:
1: Sort based on name;
2: Then sort based on age;
3: Then sort by score.
The priority is that name age score.
If the following tuples are given as input to the program:
Tom,19,80
John,20,90
Jony,17,91
Jony,17,93
Json,21,85
Then, the output of the program should be:
[(John, 20, 90), (Jony, 17, 91), (Jony, 17, 93), (Json, 21, 85), (Tom, 19, 80)]
Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
'''
person = [('Tom',19,80), ('John',20,90),('Jony',17,91),('Jony',17,93),('Json',21, 85)]

def sorting(person):
    person.sort(key = lambda x: x[0])
    return person
 
#print(sorting(person))
'''
2) Define a class with a generator which can iterate the numbers, which are divisible by 7,
between a given range 0 and n.
'''

def generator():
    n = int(input("Enter a value for n: "))
    divisible = (i for i in range(0,n) if i%7==0)
    for j in divisible: 
        print(j, end = ' ')

#generator()
'''
3) Question:
Define a function which can generate a dictionary where the keys are numbers between 1 and 20
(both included) and the values are square of keys. The function should just print the keys only.
Hints:
Use dict[key]=value pattern to put entry into a dictionary.
Use ** operator to get power of a number.
Use range() for loops.
Use keys() to iterate keys in the dictionary. Also we can use item() to get key/value pairs.
'''
dictionary = {i:j**2 for i,j in zip(range(1,21), range(1,21))}
#print(dictionary)
'''
4)
Write a program, which will find all such numbers between 1000 and 3000 (both included) such
that each digit of the number is an even number.
The numbers obtained should be printed in a comma-separated sequence on a single line.
Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.  
'''
ans = []

for number in range(1000, 3001):
	
	num_str = str(number)
	is_ok = True

	for char in num_str:
		if int(char) % 2:
			is_ok = False
			break
	if is_ok:
		ans.append(str(number))

#print(",".join(ans))

'''
1) Given list of tuples, sort by frequency of second element of tuple.
Input : test_list = [(6, 5), (1, 7), (2, 5), (8, 7), (9, 8), (3, 7)]
Output : [(1, 7), (8, 7), (3, 7), (6, 5), (2, 5), (9, 8)]
Explanation : 7 occurs 3 times as 2nd element, hence all tuples with 7, are aligned first.
Input : test_list = [(1, 7), (8, 7), (9, 8), (3, 7)]
Output : [(1, 7), (8, 7), (3, 7), (9, 8)]
Explanation : 7 occurs 3 times as 2nd element, hence all tuples with 7, are aligned first.

'''
from collections import Counter

test_list = [(6, 5), (2, 7), (2, 5), (8, 7), (9, 8), (3, 7)]
  
count = Counter(value for key, value in test_list)

output = sorted(test_list, key = lambda x: count[x[1]], reverse = True)
  
#print("Output: " + str(output))
'''
2) Given a Tuple List, perform sort on basis of total digits in tuple.
Examples:
Input : test_list = [(3, 4, 6, 723), (1, 2), (134, 234, 34)] 
Output : [(1, 2), (3, 4, 6, 723), (134, 234, 34)] 
Explanation : 2 < 6 < 8, sorted by increasing total digits.
 
Input : test_list = [(1, 2), (134, 234, 34)] 
Output : [(1, 2), (134, 234, 34)] 
Explanation : 2 < 8, sorted by increasing total digits. 

'''
def count_digs(tup):
    return sum([len(str(ele)) for ele in tup ])

test_list = [(3, 4, 6, 723), (1, 2), (12345,), (134, 234, 34)]
  
test_list.sort(key = count_digs)
  
#print("Output: " + str(test_list))
'''
3) Validate the user input using exception. Assume input from console.
I) InvalidPasswordFormatException – throw and catch this exception if an invalid password format is
entered (note: passwords must be at least eight (8) characters long and must contain at least one
asterisk (‘*’) character
II. NegativeDollarAmountException - throw and catch this exception if a negative dollar amount is
entered
iii)ATMWithdrwableLimitException- If withdraw amount is less than 100 and more than 25000
IV) MaxDepositeException- throw if Amount < 100000
'''

class CustomException(Exception):
    pass
class InvalidPasswordFormatException(CustomException):
    pass
class NegativeDollarAmountException(CustomException):
    pass
class ATMWithdrwableLimitException(CustomException):
    pass
class MaxDepositeException(CustomException):
    pass
def banking():
    try: 
        password = input("User Password: ")
        if "*" not in password or len(password) < 8:
            raise InvalidPasswordFormatException
        else: 
            try:
                withdraw = (input("Withdraw Amount: ")) 
                deposit = (input("Deposit Amount: "))
                if withdraw<0.0 or deposit<0.0:
                    raise NegativeDollarAmountException
                elif withdraw < 100.0 or withdraw > 25000.0:
                    raise ATMWithdrwableLimitException
                elif deposit < 100000.0:
                    raise MaxDepositeException
                else:
                    print("Transaction Successful")
                    
            except:
                print("Exception Error")
                
    except:
        print("Exception Error")
        
#banking()

import os
print("Name of the Operating System: ",os.name)
print("Current Working Directory: ",os.getcwd())   
print("Files and Directories in the Current Directory: ", os.listdir())
try: 
    f = open("fileName.txt", 'r')
    text = f.read()
    f.close()
except IOError as e:
    print(e)

from datetime import datetime, date, timedelta    
import time

def threeSeconds():
    for i in range(5):
        print(str(datetime.now().strftime("%H:%M:%S"))+" - String")
        time.sleep(3)
#threeSeconds()
    
def twentyDays():
    specifiedDate = date(2023, 2, 14)
    for i in range(12):
        specifiedDate+=timedelta(days=20)
        print(specifiedDate)
#twentyDays()

'''
import calendar
cal = calendar.TextCalendar(calendar.SUNDAY)

print(cal.formatyear(2022, 2, 1, 1, 3))
'''

print(datetime.fromtimestamp(1284105682).strftime("%Y:%m:%d:%H:%M:%S"))

print(datetime.today() - timedelta(days=1))

'''
1. Write a python program to find the longest words
2. Write a Python program to copy the contents of a file to another file .
3. Write a sample dictionary, list,tuple and set into a CSV file
4. Write a Python program that matches a word containing &#39;z. Read input from file and write output into a file.
5. Write a Python program to remove leading zeros from an IP address.
'''
import re

string = "Hello there, my name is mikyle and this is the longest word"
def longestWord(string):
    regex = re.compile("\w+")
    wordsFound = regex.findall(string)

    if wordsFound:
        longestWord = max(wordsFound, key=lambda word: len(word))
        print("Longest Word: " +longestWord)
#longestWord(string)

fileA = 'a.txt'
fileB = 'b.txt'

def copyContent(fileA, fileB):
    try:
        with open(fileA,'r') as firstfile, open(fileB,'a') as secondfile:
            for line in firstfile:
                    secondfile.write(line)
    except:
        print("Can't find the files")
    
#copyContent(fileA, fileB)

print(re.search('\w*z.\w*',  "i am going to the zoo tomorrow."))

print(re.sub('\.[0]*', '.', "192.05.035.194"))