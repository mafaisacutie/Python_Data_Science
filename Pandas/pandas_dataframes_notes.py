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

print(df > 0) # this will return a boolean of where each value is greater than zero
# returns
#        w      x      y      z
# a   True   True   True   True
# b   True  False  False   True
# c  False   True   True  False
# d   True  False  False   True
# e   True   True   True   True

booldf = df > 0
print(df[booldf]) # this will print out the values where ture and NaN where False
#           w         x         y         z
# a  2.706850  0.628133  0.907969  0.503826
# b  0.651118       NaN       NaN  0.605965
# c       NaN  0.740122  0.528813       NaN
# d  0.188695       NaN       NaN  0.955057
# e  0.190794  1.978757  2.605967  0.683509

# same thing
print(df[df>0])

print(df['w']>0) # this will return the 'w' series with boolean of true is greater than 0 and false else
# returns
# a     True
# b     True
# c    False
# d     True
# e     True
# Name: w, dtype: bool

print(df[df['w']>0]) # prints only rows that is greater than 0 under column 'w'
# returns
#           w         x         y         z
# a  2.706850  0.628133  0.907969  0.503826
# b  0.651118 -0.319318 -0.848077  0.605965
# d  0.188695 -0.758872 -0.933237  0.955057
# e  0.190794  1.978757  2.605967  0.683509

# grab all the rows in the dataframe where z < 0
print(df[df['z']<0])
# returns
#           w         x         y         z
# c -2.018168  0.740122  0.528813 -0.589001

# grab where 'w' is greater than 0, then grab columns 'y' 'x'
boolser = df['w']>0
result = df[boolser]
mycols = ['y','x']
print(result[mycols])
# MORE EFFECIENT WAY
print(df[df['w']>0][['y','x']]) # df where df column 'w' is greater than 0, print columns 'y' and then 'x'
# returns
#           y         x
# a  0.907969  0.628133
# b -0.848077 -0.319318
# d -0.933237 -0.758872
# e  2.605967  1.978757

# grab where x < 0 and print columns 'w' and 'z'
print(df[df['x']<0][['w','z']])
# returns
#           w         z
# b  0.651118  0.605965
# d  0.188695  0.955057

############ MULTIPLE CONDITIONAL SELECTION ####################
# IF YOU GET ERROR ambiguos THAT IS MOST LIKELY CAUSED BY USING 'and' INSTEAD OF '&' OR 'or' INSTEAD OF '|' #
# grab where 'w' > 0 and 'y' greater than 1
print(df[(df['w']>0)&(df['y']>1)])
# returns
#           w         x         y         z
# e  0.190794  1.978757  2.605967  0.683509


# INDEXING

# to reset index to numerical value
df.reset_index() # this will not overwrite current dataframe unless we specify inplace=True ex: df.reset_index(inplace=True)

# adding a column named 'States' with the index of 'newind'
newind = 'CA NY WY OR CO'.split() # .split() is sliting the blank space wot make a list
df['States'] = newind
print(df)
# returns
#           w         x         y         z States
# a  2.706850  0.628133  0.907969  0.503826     CA
# b  0.651118 -0.319318 -0.848077  0.605965     NY
# c -2.018168  0.740122  0.528813 -0.589001     WY
# d  0.188695 -0.758872 -0.933237  0.955057     OR
# e  0.190794  1.978757  2.605967  0.683509     CO

# set states as index as long as states is a column
print(df.set_index('States'))
# returns
#                w         x         y         z
# States
# CA      2.706850  0.628133  0.907969  0.503826
# NY      0.651118 -0.319318 -0.848077  0.605965
# WY     -2.018168  0.740122  0.528813 -0.589001
# OR      0.188695 -0.758872 -0.933237  0.955057
# CO      0.190794  1.978757  2.605967  0.683509
# THIS WAS NOT INPLACE, THEREFORE THE DATA IS THE SAME
print(df)
