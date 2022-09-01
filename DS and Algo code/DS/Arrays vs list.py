# Similarities
# 1. Both are mutable
# 2. Both can be iterated through
# 3. Both can be sliced

# Differences
# 1. Arrays are specialized for Arithmetic ops
import numpy as np
myList1 = [1,2,3,4]
myArray1 = np.array(myList1)
myArray1 /2   # is valid but the same op will throw error with list

# 2. lists can contain different datatypes, arrays cannot