# Array with Array
## Array with Scalers
### Universal Array Funcions


# Array with Array
import numpy as np

arr = np.arange(0,11)
# returns [ 0 1 2 3 4 5 6 7 8 9 10]
print(arr + arr)
# returns [ 0 2 4 6 8 10 12 14 16 18 20]
print(arr - arr)
# returns [ 0 0 0 0 0 0 0 0 0 0 0]

## Array with Scalers
print(arr + 100) # adds 100 to every element in the array
# returns [100 101 102 103 104 105 106 107 108 109 110]
# same for others
print(arr * 100)
print(arr-100)
print(arr**2)
print(arr%2)

### Universal Array Functions
print(np.sqrt(arr)) # sruare root of everything in the array
# returns
# [0.         1.         1.41421356 1.73205081 2.         2.23606798
#  2.44948974 2.64575131 2.82842712 3.         3.16227766]
print(np.exp(arr)) # calcs the exponential
# returns
# [1.00000000e+00 2.71828183e+00 7.38905610e+00 2.00855369e+01
#  5.45981500e+01 1.48413159e+02 4.03428793e+02 1.09663316e+03
#  2.98095799e+03 8.10308393e+03 2.20264658e+04]
print(np.max(arr)) # gets max value in the array
# returns
# 10
print(np.sin(arr)) # sin of array
# returns
# [ 0.          0.84147098  0.90929743  0.14112001 -0.7568025  -0.95892427
#  -0.2794155   0.6569866   0.98935825  0.41211849 -0.54402111]
print(np.log(arr)) # log of array
# returns
# [      -inf 0.         0.69314718 1.09861229 1.38629436 1.60943791
#  1.79175947 1.94591015 2.07944154 2.19722458 2.30258509]
# gives a warning because log of 0 is -inf
