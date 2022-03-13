#Numpy array has attribute base that returns None if the array owns the data
#If not,the base attribute refers to the original object.
from numpy import *
arr = array([1,4,7,9,2,0])
ar1 = arr.copy()
ar2 = arr.view()
print(ar1.base)     # copy returns None
print(ar2.base)     # view returns original array
# attribute called shape returns a tuple with each index having the no. of corresponding elements.
arr1 = array([[3,4,6],[4,9,0]])
print(arr1.shape) #In output 2 represents dimension of array...3 represents no.of elements
arr2 = array([[2,1,0,4,3],[8,6,5,0,4]])
print(arr2.shape)
#arr3 = array([[2,1,0,4],[8,6,5,0,4]]) #Different no.of elements in both arrays results in error.
#print(arr3.shape)
arr3 = array([2,4,6,8,10],ndmin = 5)
print(arr3)
print(arr3.shape)