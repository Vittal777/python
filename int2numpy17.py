# To search an element in an array,we use where() method...it'll return the indices of searched element.
from numpy import *
arr = array([1,3,9,8,1,2,4,9,1,5])
i = where(arr==1)
print(i)
print('\n')
i1 = where(arr%2==0)        #When elements are even
print(i1)
print('\n')
i2 = where(arr%2!=0)        #When elements are odd
print(i2)
print('\n')
# searchsorted() method is used on sorted arrays
s = searchsorted(arr,6)
print(s)