import calculator_class

obj = calculator_class.Calc(1,2)
print(obj.x,"*",obj.y,"=",obj.mul(), "\t... import")

from calculator_class import *

obj = Calc(1,2)
print(obj.x,"/",obj.y,"=",obj.div(),"\t... from import")

from collections import *

print(Counter(['A', 'B', 'C', 'A', 'B', 'C', 'A', 'A', 'B', 'A', 'B', 'C']))

OD = OrderedDict()
OD['a'] = 1
OD['b'] = 2
OD['c'] = 3

for key, value in OD.items():
    print(key,":", value,"|",end=' ')
    
print("")

OD.pop('a')
OD['a'] = 1
for key, value in OD.items():
    print(key,":", value,"|", end=' ')

print("")

DE = deque([5,4,34,41,2])
DE.pop()
print(DE)

DE.popleft()
print(DE)
       
from functools import *

class Demo:
    def __init__(self):
        self.color = "black"
    def _color(self,type):
        self.color =type
    set_red = partialmethod(_color, type="red")
    set_blue = partialmethod(_color, type="blue")
    set_green = partialmethod(_color, type="green")
    
obj = Demo()
print(obj.color)
obj.set_red()
print(obj.color)
obj._color("grey")
print(obj.color)

import itertools

for x in itertools.count(1,1): # range(0,100, 5):
    print(x, end=' ')
    if x >= 10:
        break
print('')
count = 0
for x in itertools.cycle('abcde'): # range(0,100, 5):
    print(x, end=' ')
    count += 1
    if count >= 10:
        break
print('')
print(list(itertools.repeat(25,10)))
print(list(itertools.product([1,2], repeat = 2)))
print(list(itertools.product(['hi', 'for', 'hello'], '2')))
print(list(itertools.product('AB', [3,4])))

li = [2,4,5,7,8,10,20]

print(list(itertools.islice(li, 1,6,2)))
print(list(itertools.takewhile(lambda x: x%2 == 0, li))) # its like do while ...

li = [(1,10,5), (8,4,1), (5,4,9), (11,10,1)]
print(list(itertools.starmap(max, li)))