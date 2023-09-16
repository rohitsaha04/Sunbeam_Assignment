# Q4.Write a Pandas program to change the order of index of a given series. Go to
# the editor
# Sample Output:
# Original Data Series:
# A1
# B2
# C3
# D4
# E5
# dtype: int64
# Data Series after changing the order of index:
# B2
# A1
# C3
# D4
# E5
# dtype: int64

import pandas as pd

numbers = pd.Series([ 1, 2, 3, 4, 5 ], index = [ 'A1', 'B2', 'C3', 'D4', 'E5'])
numbers = numbers.reindex(index = ['B2', 'A1', 'C3', 'D4', 'E5'])
print(numbers)


