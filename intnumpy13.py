# Joining arrays
from numpy import *
arr1 = array([3,6,9,4,0])
arr2 = array([5,7,2,1,3])
add = concatenate((arr1,arr2))
print(add)
print('\n')
# joining 2D arrays using axis = 1
arr3 = array([[3,2,1],[5,9,0]])
arr4 = array([[3,0,6],[5,2,1]])
add1 = concatenate((arr3,arr4),axis=1)
print(add1)
print('\n')
# Using stack() function, same as concatenation only difference is it is done along a new axis,if axit isn't explicitly passed,
#it will be considered as 0.
add2 = stack((arr3,arr4),axis=2)
print(add2)
print('\n')
add3 = stack((arr3,arr4),axis=1)
print(add3)
print('\n')
add4 = stack((arr3,arr4)) #axis didn't explicitly passed,so by default 0 will be considered.
print(add4)
print('\n')
#add5 = stack((arr3,arr4),axis=3) # axis 3 is out of bound for array of dimension 3
#print(add5)