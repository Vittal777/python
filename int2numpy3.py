#Accessing 1D,2D,3D array elements
from numpy import *
arr = array([4,6,9,0,1])
print(arr[3],arr[1]) #Accessing elements by indexing
print(arr[2]+arr[4]) #Adding 2 elements of an array
print(arr[1]+arr[3]+arr[0]) #Adding 3 elements of an array
arr1 = array([[4,5,8],[1,9,5]])
print(arr1[0,2],arr1[1,1]) #Accessing 2D elements...
print(arr1[0,1]+arr1[1,0])
arr2 = array([[[2,3,4],[5,9,0]],[[3,2,1],[3,5,7]]])
print(arr2[0,0,2])
print(arr2[1,1,1])
print(arr2[0,1,1])
print(arr2[1,0,2])