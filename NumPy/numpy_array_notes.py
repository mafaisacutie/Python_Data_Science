import numpy as np

# NumPy Arrays
# Vectors are strictly 1-d and matricies are 2-d
my_list = [1,2,3]
arr = np.array(my_list)
print(arr)

# make a 2-d array
my_mat=[[1,2,3],[4,5,6],[7,8,9]]
print(my_mat)
print(np.array(my_mat))
# returns
# [[1 2 3]
#  [4 5 6]
#  [7 8 9]]
# you can tell it is a 2-d array by the amount of beginning brackets

# create an array
print(np.arange(0,10)) # create an array with [ 0,1,2,3,4,5,6,7,8,9 ]
print(np.arange(0,11,2)) # creates an even number array 0-10 | returns [ 0  2  4  6  8 10]

# generate array of all zeros
print(np.zeros(3))
# returns [0. 0. 0.]
print(np.zeros((5,5))) # pass a tuple into the argument to create an array specifying (rows,columns)
# returns
# [[0. 0. 0. 0. 0.]
#  [0. 0. 0. 0. 0.]
#  [0. 0. 0. 0. 0.]
#  [0. 0. 0. 0. 0.]
#  [0. 0. 0. 0. 0.]]

# make an array of all zeros with 6 rows and 9 columns with NumPy
print(np.zeros((6,9)))
# returns
# [[0. 0. 0. 0. 0. 0. 0. 0. 0.]
#  [0. 0. 0. 0. 0. 0. 0. 0. 0.]
#  [0. 0. 0. 0. 0. 0. 0. 0. 0.]
#  [0. 0. 0. 0. 0. 0. 0. 0. 0.]
#  [0. 0. 0. 0. 0. 0. 0. 0. 0.]
#  [0. 0. 0. 0. 0. 0. 0. 0. 0.]]

# same with np.ones()
print(np.ones((3,4)))
# returns
# [[1. 1. 1. 1.]
#  [1. 1. 1. 1.]
#  [1. 1. 1. 1.]]

# linspace
print(np.linspace(0,5,10)) # np.linspace(start, stop, num)
# returns
# [0.         0.55555556 1.11111111 1.66666667 2.22222222 2.77777778
#  3.33333333 3.88888889 4.44444444 5.        ]

# identity matrix
print(np.eye(4)) # np.eye(digit)
# returns
# [[1. 0. 0. 0.]
#  [0. 1. 0. 0.]
#  [0. 0. 1. 0.]
#  [0. 0. 0. 1.]]
# makes a square matrix with diag ones

# Generate an array with random numbers
print(np.random.rand(5))# random 1d matrix between 0-1
# Example
# [0.67232945 0.94580144 0.62096216 0.19107677 0.0537932 ]
print(np.random.rand(5,5)) # random 2d matrix betwween 0-1
# Example
# [[0.73570521 0.21784386 0.70688464 0.14486232 0.53074281]
#  [0.77911275 0.22179442 0.423973   0.55728021 0.66152942]
#  [0.85767471 0.4082625  0.39517667 0.1079403  0.70582763]
#  [0.06647303 0.28309529 0.81290949 0.27781128 0.25597692]
#  [0.55779362 0.90232428 0.42223258 0.02772879 0.25780539]]
print(np.random.randn(4,4))
# returns random integers from high to low
print(np.random.randint(1,100)) # np.random.randint(low, high, size, dtype='')
# returns random number from 1 to 100
# 1 has a chance of being selected, 100 does not. 100 is exclusive, 1 is inclusive
print(np.random.randint(1,100,10)) # same thing, but it selects 10 randoms now

# Attributes and methods of an array
ranarr = np.random.randint(0,50,10) # 10 random array items from 0 to 50
arr = np.arange(25) # 0-25, not including 25
print(arr.reshape(5,5)) # reshapes the 1d 25 to a 2d 5,5
                 # rows*columns = arrayTotal
                 # 5*5 = 25

# finding max and min
print(ranarr.max()) # returns the maximum value in the array
print(ranarr.min()) # returns the minimum value in the array
# Grab the location of the min and max
print(ranarr.argmax()) # returns the position location of the max value
print(ranarr.argmin()) # returns the position location of the min value
print(arr.shape) # returns the shape of the array
# returned (25,) <- no second arg means it is 1d
# make arr a 5,5 array
print(arr.reshape(5,5))
print(arr.shape) # returns (5, 5)

# Data type
print(arr.dtype) # returns the data type of the array
# returns int32
