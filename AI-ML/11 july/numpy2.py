import numpy as np
print(np.random.random((1,4)))
print(np.random.random((3,4)))


m=np.random.uniform(low=3,high=4,size=(5,2)) #this will print the values between 3 to 4 in 5,2 matrix
print(m)

n=np.linspace(10,20,5) #this function is used to print the values at equal distance:(start,end,how many item we want to generate)
print(n)

print(n.dtype)


o=np.identity(3)
print(o)