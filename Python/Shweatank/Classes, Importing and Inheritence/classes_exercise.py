# Write a Python program to import a built-in array module and display the namespace of the said module
import array
for namespace in array.__dict__:
    print(namespace)

# Write a Python program to create a class and display the namespace of that class

# Write a Python class named Student with two instances student1, student2 and assign values to the instances' attributes. Print all the attributes of the student1, student2 instances with their values in the given format.
class Student:
    def __init__(self, name, age, school):
        self.name = name
        self.age = age
        self.school = school 
        
    def print_attributes(self):
        print("Name: ", self.name, "| Age: ", self.age, " | School: ", self.school)
        
student1 = Student("Bob", 18, "UWC")
student2 = Student("Meg", 24, "UCT")

student1.print_attributes()
student2.print_attributes()

'''
# also try this sometime, when there are a lot of students ...
students = [student1, student2]
for student in students:
    for attr in student.__dict__:
        print(f'{attr} : {getattr(student, attr)}')
'''

# Write a Python class to get all possible unique subsets from a set of distinct integers
class py_solution:
    def sub_sets(self, sset):
        return self.subsetsRecur([], sorted(sset))
    
    def subsetsRecur(self, current, sset):
        if sset:
            return self.subsetsRecur(current, sset[1:]) + self.subsetsRecur(current + [sset[0]], sset[1:])
        return [current]

print(py_solution().sub_sets([4,5,6]))
# Input : [4, 5, 6]Output : [[], [6], [5], [5, 6], [4], [4, 6], [4, 5], [4, 5, 6]]

# Write a Python class to reverse a string word by word
class reverse:
    def __init__(self, the_string):
        self.the_string = the_string
        self.__reversed_string = ""
    def reverse(self):
        reversed_string = self.the_string.split()[::-1]
        all_words = []
        for word in reversed_string:
            all_words.append(word)
        self.__reversed_string = " ".join(all_words)
    def get_reversed_string(self):
        return self.__reversed_string

test = reverse("hello there")
test.reverse()
print(test.get_reversed_string())