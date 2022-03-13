#Data types in numpy
from numpy import *
arr = array([4,5,6])
print(arr.dtype)
arr1 = array([3.2,4.8,1.5])
print(arr1.dtype)
arr2 = array(['V','I','T','T','A','L'])         #Unicode string
print(arr2.dtype)
arr3 = array(['abc','xyz','def'])
print(arr3.dtype)
#Creating with defined data type
arr4 = array([3,4,5,7,9],dtype = 'S')
print(arr4) 
print(arr4.dtype)
arr5 = array([4,1,0,9],dtype = 'i4')            #4 bytes integer
print(arr5)
print(arr5.dtype)
arr6 = array([4,1,0,9],dtype = 'i')            #4 bytes integer
print(arr6)
print(arr6.dtype)
arr7 = array([4,1,0,9],dtype = 'i8')            #4 bytes integer
print(arr7)
print(arr7.dtype)