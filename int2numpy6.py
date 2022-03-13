from numpy import *
#arr = array(['Vittal','4',1.3],dtype = 'i') # Non-integer string 'Vittal' can't be converted to integer
#print(arr)
# astype() function creates a copy of array,and allows you to specify data type as a parameter.
#parameters can 'f' for float and 'i' for integer or directly float for float and int for integer.
arr = array([1,9,0,8,7])
arr1 = arr.astype('f')
arr2 = arr.astype(str)
arr3 = arr.astype(bool)
print(arr1)
print(arr2)
print(arr1.dtype)
print(arr2.dtype)
print(arr3)
#copy owns the data and any changes made to the copy won't affect the original array anad vice-versa.
#view do not own the data and any changes made to the view will affect the original array.
arr4 = array([[4,5,9],[1,0,8]])
ar = arr4.copy()
arr4[1,2] = 10
print(arr4)         #Original array
print(ar)           #Copied array
arr5 = array([2,5,7,9,1,0])
ar1 = arr5.view()
arr5[3] = 10
print(arr5)
print(ar1)
