#SHAPE AND RESHAPE OF THE ARRAY.
import numpy as np
x=np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])

print(x)
new=np.reshape(x,(2,5,-1))
print(new)
print(new.shape)