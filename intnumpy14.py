# Stacking along rows using hstack() function
from numpy import *
arr1 = array([4,7,9])
arr2 = array([4,2,0])
add = hstack((arr1,arr2))
print(add)
print('\n')
# Stacking along columns using vstack() function
add1 = vstack((arr1,arr2))
print(add1)
print('\n')
# Stacking along height using dstack() function
add2 = dstack((arr1,arr2))
print(add2)