# Random permutation of elements is done by shuffle() and permutation() methods.
# shuffle() make changes to original array,whereas permutation() returns rearranged array.
from numpy import *
arr = array([6,4,1,0,9,7])
random.shuffle(arr)
print(arr,'\n')
ar = random.permutation(arr)
print(ar)