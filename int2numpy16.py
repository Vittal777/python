# Splitting of 2D arrays
from numpy import *
arr = array([[5,6,7],[9,0,1],[3,7,1],[0,3,1]])
spl = array_split(arr,3)
print(spl)
print('\n')
spl1 = array_split(arr,5)
print(spl1)
print('\n')
spl2 = array_split(arr,2)
print(spl2)
print('\n')
# Splitting is done by by along rows,columns and depth by using hsplit(),vsplit() and dsplit() respectively.
arr1 = array([[5,6,7],[9,0,1],[3,7,1],[0,3,1]])
spl3 = hsplit(arr1,3)           #for rows
print(spl3)
print('\n')
arr2 = array([[5,6,7],[9,0,1],[3,7,1],[0,3,1]])
spl4 = vsplit(arr,2)
print(spl4)
print('\n')
#spl5 = vsplit(arr,3)    Array split doesn't result in equal division
#print(spl5)
arr3 = array([[[5,6,7],[9,0,1]],[[3,7,1],[0,3,1]]])
#spl5 = dsplit(arr3,3) #dsplit works only on 3 or multiD arrays
#print(spl5)
spl5 = dsplit(arr3,3)
print(spl5)