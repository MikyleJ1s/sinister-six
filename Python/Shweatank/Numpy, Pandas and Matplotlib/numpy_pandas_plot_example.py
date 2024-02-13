import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from pylab import *

dt = np.dtype([('age', np.int8)])
a = np.array([(10,), (20,), (30,)], dtype=dt)
print(a['age'])

student = np.dtype([('name', 'S20'), ('age', 'i1'), ('marks', 'f4')])
print(student)

c = [1,2,3,5,2,8,0]

plt.plot(c)
plt.show()

x = np.linspace(-3,3, 30)
print(x)
y = x*x
plt.plot(x,y, 'r.')
plt.show()

plot(x, sin(x)) 
plot(x, cos(x), 'r-') 
plot(x, -sin(x), 'g--') 
show()

N = 5
menMeans = (20, 35, 30, 35, 27)
womenMeans = (25, 32, 34, 20, 25)
ind = np.arange(N) # the x locations for the groups
width = 0.35
fig=plt.figure()
ax=fig.add_axes([0,0,1,1])
ax.bar(ind, menMeans, width, color='r')
ax.bar(ind, womenMeans, width,bottom=menMeans, color='b')
ax.set_ylabel('Scores')
ax.set_title('Scores by group and gender')
ax.set_xticks(ind, ('G1', 'G2', 'G3', 'G4', 'G5'))
ax.set_yticks(np.arange(0, 81, 10))
ax.legend(labels=['Men', 'Women'])
plt.show()

f = ['FB', '2001-08-02', 90, 3.2]
f = pd.Series(f, index = ['name', 'date', 'shares', 'price'])
print(f)

data = {'name': ['AA', 'IBM', 'GOOGLE'], 
        'date': ['2001-12-01', '2012-02-10', '2010-04-09'], 
        'shares': [100, 30, 90]}

