# Iteration using ndemunerate() means mentioning sequence number of something 1 by 1.
from numpy import *
arr = array([5,6,7,9,0,1,2])
for seq,i in ndenumerate(arr):
    print(seq,i)
print('\n')
# for 2D arrays
arr1 = array([[4,6,1,3,0],[9,7,2,5,8]])
for seq,j in ndenumerate(arr1):
    print(seq,j)
# Joining 2 arrays using concatenate() function
arr = array([6,8,9,7,0])
arr1 = array([1,2,3,5])
add = concatenate(arr,arr1)
print(add)