##### DataFrames #####
import numpy as np
import pandas as pd
from numpy.random import randn

np.random.seed(101) # like a minecraft map seed. this will always have the same random numbers

df = pd.DataFrame(randn(5,4),['a','b','c','d','e'],['w','x','y','z']) # pd.DataFrame(data=None, index=None, columns=None, dtype=None, copy=False)
print(df)
# returns
#           w         x         y         z
# a  2.706850  0.628133  0.907969  0.503826
# b  0.651118 -0.319318 -0.848077  0.605965
# c -2.018168  0.740122  0.528813 -0.589001
# d  0.188695 -0.758872 -0.933237  0.955057
# e  0.190794  1.978757  2.605967  0.683509

print(df['w'])
# returns
# a    2.706850
# b    0.651118
# c   -2.018168
# d    0.188695
# e    0.190794
# Name: w, dtype: float64

print(type(df['w']))
# returns
# <class 'pandas.core.series.Series'>

print(type(df))
# returns
# <class 'pandas.core.frame.DataFrame'>

print(df[['w','z']])
# returns
#           w         z
# a  2.706850  0.503826
# b  0.651118  0.605965
# c -2.018168 -0.589001
# d  0.188695  0.955057
# e  0.190794  0.683509

# print(df['new']])  KeyError: 'new' | This means the key is not in the DataFrame

df['new'] = df['w']+df['y']
print(df)
# returns
#           w         x         y         z       new
# a  2.706850  0.628133  0.907969  0.503826  3.614819
# b  0.651118 -0.319318 -0.848077  0.605965 -0.196959
# c -2.018168  0.740122  0.528813 -0.589001 -1.489355
# d  0.188695 -0.758872 -0.933237  0.955057 -0.744542
# e  0.190794  1.978757  2.605967  0.683509  2.796762

# df.drop('new') creates ValueError: labels ['new'] not contained in axis
print(df.drop('new',axis=1)) # axis=1 means column, it is default 0 which is rows
# returns
#           w         x         y         z
# a  2.706850  0.628133  0.907969  0.503826
# b  0.651118 -0.319318 -0.848077  0.605965
# c -2.018168  0.740122  0.528813 -0.589001
# d  0.188695 -0.758872 -0.933237  0.955057
# e  0.190794  1.978757  2.605967  0.683509

# The above^ df.drop('new',axis=1) does not affect the actual table
df.drop('new',axis=1,inplace=True) # this will permanately drop 'new' from df
print(df)

print(df.drop('e')) # drops the row 'e'
# returns
#           w         x         y         z
# a  2.706850  0.628133  0.907969  0.503826
# b  0.651118 -0.319318 -0.848077  0.605965
# c -2.018168  0.740122  0.528813 -0.589001
# d  0.188695 -0.758872 -0.933237  0.955057

# to grab a row
print(df.loc['c'])
# returns
# w   -2.018168
# x    0.740122
# y    0.528813
# z   -0.589001
# Name: c, dtype: float64
# OR
print(df.iloc[2])
# returns
# w   -2.018168
# x    0.740122
# y    0.528813
# z   -0.589001
# Name: c, dtype: float64

# grab row c column x
print(df.loc['b','x'])
# returns
# -0.31931804459303326

# grab rows b,d and columns x,z
print(df.loc[['b','d'],['x','y']])
# returns
#           x         y
# b -0.319318 -0.848077
# d -0.758872 -0.933237
