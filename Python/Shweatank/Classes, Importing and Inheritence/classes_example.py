class something:
    def __init__(self): # this is a constructor ...
        self.x = 0
        self.y = 0
        print("Hello there")
        
    def display(self):
        print("Here I will display: ", self.x, "and", self.y)
        
    def __del__(self):
        print("Here is a destructor")
        
obj1 = something() # creating object 1 ...
obj1.x = 5
obj1.y = 1

obj2 = something() # creating object 2 ...

obj3 = something() # creating object 3 ...
obj3.x = "a"
obj3.y = 3

obj1.display()
obj2.display()
obj3.display()

del obj1

print("Done")

class student:
    def __init__(self, name, age): # this is a constructor ...
        self.name = name
        self.age = age
        
    def display(self):
        print("Name: ", self.name, "| Age", self.age)
        
    def get_age(self):
        return self.age
    
    def get_name(self):
        return self.name
        
obj1 = student("Bob", 18) # creating object 1 ...
obj2 = student("Tom", 24) # creating object 2 ...

obj1.display()
obj2.display()

print("The get_name() method: ",obj2.get_name())
print("Get attribute: ", getattr(obj2, "name"))
print("Has attribute: ", hasattr(obj2, "surname"))

print("Done")
