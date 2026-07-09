#Slicing: Create a 5×5 array of sequential integers. Extract the middle 3×3 sub-array, and separately extract just the border elements.
import numpy as np
arr=np.arange(25).reshape(5,5)
print(arr)

t=arr[1:4,1:4]
print(t)

z=arr[0:1,:]
print(z)

y=arr[:,4:]
print(y)

q=arr[:,0:1]
print(q)

x=arr[4:,:]
print(x)