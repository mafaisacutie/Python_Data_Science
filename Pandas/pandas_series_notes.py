##### SERIES #####
import numpy as np
import pandas as pd


labels = ['a','b','c']
my_data = [10,20,30]
arr = np.array(my_data)
d = {'a':10,'b':20,'c':30}

print(pd.Series(data=my_data)) #pd.Series(data=None, Index=None, dtype=None, name=None, copy=False, fastpath=False)
# returns
# 0    10
# 1    20
# 2    30
# dtype: int64
print(pd.Series(data=my_data,index=labels))
# returns
# a    10
# b    20
# c    30
# dtype: int64

# or
# print(pd.Series(my_data,labels))
print(pd.Series(arr,labels))
# returns
# returns
# a    10
# b    20
# c    30
# dtype: int32

print(pd.Series(d))
# returns
# a    10
# b    20
# c    30
# dtype: int64

ser1 = pd.Series([1,2,3,4],['USA','Germany','USSR','Japan'])
print(ser1)
# returns
# USA        1
# Germany    2
# USSR       3
# Japan      4
# dtype: int64

ser2 = pd.Series([1,2,5,4],['USA','Germany','Italy','Japan'])
print(ser2)
# returns
# USA        1
# Germany    2
# Italy      5
# Japan      4
# dtype: int64

print(ser1['USA'])
# returns
# 1

print(ser1 + ser2)
# returns
# Germany    4.0
# Italy      NaN
# Japan      8.0
# USA        2.0
# USSR       NaN
# dtype: float64
# NaN means that the key is not in both series
