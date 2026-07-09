#Identity & diagonal: Create a 6×6 identity matrix, then modify it so the diagonal reads 1 through 6 instead of all 1s.

import numpy as np


arr = np.eye(6)
print("Identity matrix:")
print(arr)

np.fill_diagonal(arr, np.arange(1, 7))
print("\nModified matrix:")
print(arr)
