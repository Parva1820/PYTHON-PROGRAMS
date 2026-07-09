#Boolean masking: Given a random array of 50 integers between -50 and 50, replace all negative values with 0 using a mask (no loops).

import numpy as np
from numpy.random import random
arr=np.random.randint(-50,50,size=(50))
print(arr)

mask=arr<0
arr[mask]=0
print(arr)