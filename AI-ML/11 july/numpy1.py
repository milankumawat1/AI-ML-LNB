import numpy as np

'''

arr=np.array([1,2,3,4,5]) #1D array
print(arr)
print(arr.shape)
print(arr.dtype)

matrix=np.array([[1,2,3],[4,5,6]]) #2D array
print(matrix)
print(matrix.shape)
print(matrix.dtype)

r=np.arange(10)
print(r)
print(r.shape)
print(r.dtype)

t=np.array([[[1,2],[3,4]],[[5,6],[7,8]]]) #3D Array or tensor
print(t)
print(t.shape) #(dimentions of sub array, row,columns)
print(t.dtype)
print(t.reshape(4,2))


arr1=np.array([1,2,3])
arr2=np.array([4,5,6])
r=arr1+arr2

print(r)

arr1=np.array([1,2,3])
arr2=np.array([4,5,6])
r=arr1-arr2

print(r)

arr1=np.array([1,2,3])
arr2=np.array([4,5,6])
r=arr1*arr2

print(r)

arr1=np.array([1,2,3])
arr2=np.array([4,5,6])
r=arr1/arr2

print(r)


c=np.arange(1,13).reshape(3,4)
print(c)

c=np.arange(1,15).reshape(2,7)
print(c)

c=np.arange(1,15).reshape(7,2)
print(c)

'''

