import numpy as np

arr = np.arange(0,11) # 0 to 10
print(arr[8]) # returns array item at index 8
print(arr[1:5]) # returns [ 1 2 3 4 ]
print(arr[0:5]) # returns [ 0 1 2 3 4]
print(arr[:6]) # returns everything up to index 6
print(arr[0:6]) # same thing as above ^
print(arr[5:]) # returns everything after index 5 excluding index 5

# Broadcast an array, something a python list CAN NOT do
arr[0:5] = 100 # this "broadcasts" the items selected with the slice to be 100
print(arr)
# returns
# [100 100 100 100 100   5   6   7   8   9  10]
arr = np.arange(0,11)

# slices
slice_of_arr = arr[0:6]
print(slice_of_arr)
slice_of_arr[:] = 99 # makes everything in the matrix 99
print(slice_of_arr)
# but that also affected the original arr array
# so it is just a view of the array
print(arr)
# returns
# [99 99 99 99 99 99  6  7  8  9 10]
# this is to avoid memory issues with large arrays
# this is to copy an array
print(arr)
arr_copy = arr.copy()
print(arr_copy)
# change the copied arrayg
arr_copy[:] = 100
# since this is a copy, the original array wont be affected
print(arr_copy)
# ^ arr_copy looks like this
# [100 100 100 100 100 100 100 100 100 100 100]
# and arr looks like this
# [99 99 99 99 99 99  6  7  8  9 10]

# Indexing a 2d array aka Matrix
arr_2d = np.array([[5,10,15],[20,25,30],[35,40,45]]) # creating a 2d array aka Matrix
# returns
# [[ 5 10 15]
#  [20 25 30]
#  [35 40 45]]
print(arr_2d)
# Grab the digit 5 from the array
print(arr_2d[0][0]) # arr_2d[row][column]
# returns 5
# Grab digit 30
print(arr_2d[1][2]) # first row is 0, that means [1] is row 2 and [2] is column 3
# Grab entire second row
print(arr_2d[1])
# these can also be done with a single bracker (best way)
print(arr_2d[0,0]) # returns 5
print(arr_2d[1,2]) # returns 30

# Grab a slice of an array
# get the top right [[ 10 15 ]
#                    [ 25 30 ]]
print(arr_2d[:2,1:]) # grab everything in the rows up 2, not including 2. then grab everything from column to the end

# Slice Practices
print(arr_2d[1:3,:])
# returns
# [[20 25 30]
#  [35 40 45]]
print(arr_2d[1:,1:])
# returns
# [[25 30]
#  [40 45]]
print(arr_2d[1:,:2])
# returns
# [[20 25]
#  [35 40]]
prac = np.array([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20]])
print(prac)
# returns
# [[ 1  2  3  4  5]
#  [ 6  7  8  9 10]
#  [11 12 13 14 15]
#  [16 17 18 19 20]]
print(prac[1:3,1:3])
# returns
# [[ 7  8]
#  [12 13]]
print(prac[2:,2:4])
# returns
# [[13 14]
#  [18 19]]
print(prac[1:3,2:4])
# returns
# [[ 8  9]
#  [13 14]]

# conditional selection
arr = np.arange(1,11)
print(arr)
# returns
# [ 1  2  3  4  5  6  7  8  9 10]
bool_arr = arr > 5
print(bool_arr)
# returns
# [False False False False False  True  True  True  True  True]
print(arr[bool_arr]) # returns only True items
# returns
# [ 6  7  8  9 10]
# same thing as
print(arr[arr>5]) # <- used most
print(arr[arr<3])
# returns
# [1 2]

# MORE PRACTICES
arr = np.arange(100).reshape(5,20)
print(arr)
# returns
# [[ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19]
#  [20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39]
#  [40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59]
#  [60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79]
#  [80 81 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96 97 98 99]]

print(arr[2:4,10:12])
# returns
# [[50 51]
#  [70 71]]

print(arr[1:3,3:11])
# returns
# [[23 24 25 26 27 28 29 30]
#  [43 44 45 46 47 48 49 50]]

print(arr[:2,16:])
# returns
# [[16 17 18 19]
#  [36 37 38 39]]
