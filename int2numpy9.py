# Unknown dimension means you need not specify exact number for one of the dimension in reshape method
# Pass -1 as value, NumPy will calculate the exact number.
from numpy import *
arr  = array([3,4,1,4,5,8,9,0,2,4,5,6])
ar = arr.reshape(2,2,-1)
ar1 = arr.reshape(2,3,-1)
print(ar)
print(ar1)
# Flattening the array means converting multidimensional to 1D array,can be done by reshape(-1).
arr1 = array([[3,2,1,4],[4,8,9,0]])
arr2 = array([[[3,4],[9,0]],[[2,1],[8,7]]])
ar3 = arr2.reshape(-1)
ar2 = arr1.reshape(-1)
print(ar2)
print(ar3)
# I T E R A T I O N S
arr3 = array([5,6,7,8,9,0,1]) # Iterated 1D array
for i in arr3:
    print(i)
arr4 = array([[3,5,6,7],[6,0,9,3]])
for j in arr4:
    print(j)
arr5 = array([[[6,5,3],[4,9,8]],[[6,2,1],[8,7,4]]])
for k in arr5:
    print(k)