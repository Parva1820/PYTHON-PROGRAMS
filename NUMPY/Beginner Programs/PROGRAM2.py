#built-in vectorized functions
import numpy as np
from numpy import random

arr=np.random.randint(0,50,size=(2,5))
print(arr)
maximum=np.max(arr)
print(maximum)

minimum=np.min(arr)
print(minimum)

mean_arr=np.mean(arr)
print(mean_arr)

median_arr=np.median(arr)
print(median_arr)