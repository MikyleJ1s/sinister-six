class student:
    def __init__(self, name, age):
        self.studentname = name # public
        #self._studentname = name # protected
        #self.__studentname = name # private
        self.studentage = age
        
    def displayStudent(self):
        print(self.studentname)
    
objectStudent = student("John", 23)
print(objectStudent.studentname)

n = 20
print(bin(n)) # binary
print(oct(n)) # octa
print(hex(n)) # hexadecimal

print(ord("1")) # unicode/ascii code