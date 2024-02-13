class AO(): 
    x = 0
    
    def print_x(self):
        print(self.x)
class BO(AO): 
    x = 1
class CO(AO): 
    x = 2
class DO(BO, CO): 
    pass
    
obj = AO()
obj.print_x()

obj = BO()
obj.print_x()

obj = CO()
obj.print_x()

obj = DO()
obj.print_x()

class Calc_Basics:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def add(self):
        return self.x+self.y
    
    def sub(self):
        return self.x-self.y
    
    def print_data(self):
        print("Data from parent class")
    
class Calc_Advanced(Calc_Basics):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        # super().__init__(x,y) ... can use this also instead of the two above lines
        
    def mul(self):
        return self.x*self.y
    
    def div(self):
        return self.x/self.y
    
    def print_data(self):
        print("Data from child class")
    
obj_bas = Calc_Basics(10,20)
print("Basic Sum Operation:", obj_bas.add())  

obj_adv = Calc_Advanced(30,20)
print("Advanced Sum Operation:", obj_adv.add())

class Animals:
    def __init__(self):
        self.legs = 4
        self.domestic = True
        self.tail = True
        self.mammal = True
        self.__eyes = 2
        
    def isMammal(self):
        if self.mammal:
            print("It is a mammal")
            
    def isDomestic(self):
        if self.domestic:
            print("It is a domestic animal")
            
    def print_data(self):
        print("Legs: ", self.legs)
        print("Eyes: ", self.__eyes)
        
    def get_eyes(self):
        return self.__eyes
    
class Dogs(Animals):
    def __init__(self):
        super().__init__()
    def isMammal(self):
        super().isMammal()
        
class Horses(Animals):
    def __init__(self):
        super().__init__()
        
    def hasTailsandLegs(self):
        if self.tail and self.legs == 4:
            print("It has a tail and legs")
            
tom = Dogs()
tom.isMammal()

bruno = Horses()
bruno.hasTailsandLegs()

cat = Animals()
cat.print_data()

print(cat.legs)

# print(cat.__eyes) does not work

print(cat.get_eyes())