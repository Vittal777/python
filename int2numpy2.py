#To check no of dimensions
from numpy import *
arr1 = array(34)
arr2 = array([4,8])
arr3 = array([[2,6],[9,8]])
arr4 = array([[[4,6],[2,1]],[[4,3],[8,0]]])
print(arr1.ndim)
print(arr2.ndim)
print(arr3.ndim)
print(arr4.ndim)
#Creating an array with required dimensions
from numpy import *
arr = array([2,5,7,9,0],ndmin = 4)
print(arr)
print(arr.ndim)
arr1 = array([2,5,7,9,0],ndmin = 6)
print('No. of dimensions :',arr1.ndim)
print(arr1)