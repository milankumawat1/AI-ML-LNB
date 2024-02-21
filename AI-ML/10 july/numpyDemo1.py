'''
Numpy: numeric python

it provides support for a large multidimentional array and matrics along with collection of mathematical function to operate on these array efficiently.


Need:

    Array:
    Numerical Operation: log and exp operations 
    Efficiency: Faster performance than list
    Broadcasting:
    Integration with libraries:

    
Numpy vs List:

    Numpy is fixed and list is dynamic
    Numpy is homogeneous and List contains all tyoes of data
    Numpy perform difficult operations easily and list require large coding to perform the same operation
    Numpy stores value rather than address


'''

# '''

import time

a=[i for i in range(100000)]
b=[i for i in range(100000,200000)]
c=[]

start1=time.time()
for i in range(len(a)):
    c.append(a[i]+b[i])

print(c)

print(time.time()-start1)
# '''


import numpy as np
x=np.arange(100000)
y=np.arange(100000,200000)
start2=time.time()
z=x+y
print(z)

print(time.time()-start2)
