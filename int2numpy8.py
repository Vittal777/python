# Reshaping is changing the shape of an array,i.e,we can add or remove,or can change the no. of dimensions.
from numpy import *
arr = array([4,6,7,9,0,1,2,3])
ar = arr.reshape(4,2) # 4 is no.of arrays...2 is nno.of elements in each array.
#ar1 = arr.reshape(3,2) #Can't reshape
print(ar)
#print(ar1)
arr1 = array([5,6,7,8,9,0,8,6,7,5,1,2])
ar1 = arr1.reshape(2,3,2)
print(ar1)
#Elements required for reshaping should be equal in both shapes.
#We can reshape 8 elements 1D array into 4 elements in 2 rows 2D array but we can't reshape it into 3 elements 3 rows 2D array as it requires 9 elements.
arr2 = array([5,6,7,1,2,3])
ar2 = arr2.reshape([3,2]).base
print(ar2)