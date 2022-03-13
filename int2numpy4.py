#Accessing array elements using slicing
from numpy import *
arr = array([4,6,9,0,1,2]) #Accessing 1D elements,by
print(arr[1:5])             #Positive slicing
print(arr[-4:])             #Negative slicing
arr1 = array([[3,5,6,1,6],[4,3,8,7,6]])
print(arr1[1,0:3])
print(arr1[0,0:4:2])