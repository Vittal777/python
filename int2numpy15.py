# splitting of arrays is done using array_split(),the arguments are array and the no. of splits we need.
from numpy import *
arr = array([3,7,9,0,4,2,1,5])
spl = array_split(arr,2)
spl1 = array_split(arr,4)
print(spl)
print('\n')
print(spl1)
print('\n')
arr1 = array([2,3,5,6,7,8,9,0])
spl2 = array_split(arr1,5)  #If the array has less elements than required,it will adjust from end accordingly.
print(spl2)
print('\n')
# We also have split() function but it won't adjust elements when elements are less in source array.
# Accessing elements in split arrays
print(spl2[0])
print(spl2[1])
print(spl2[2])
print(spl2[3])
print(spl2[4])