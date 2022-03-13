# Iterating arrays with different data types
from numpy import *
# We can use op_dtypes argument, pass it the expected datatype to change the data type of elements while iterating.
#NumPy doesn't change the datatype of elements in-place so it needs some other space to perform the action,
# That extra space is called Buffer,and to enable it in nditer(), we pass flags = ['buffered']
arr = array([4.6,2.5,9.1,6.7]) # We can't typecast from float64 to int32 or int64
for i in nditer(arr,flags = ['buffered'],op_dtypes = ['S']):
    print(i)   
print('\n')
# Iterating with different step size
arr1 = array([[4,3,5,6,7],[1,2,8,9,0]])
for j in nditer(arr1[:,::2]):
    print(j,'\n')
    for k in nditer(arr1[:,::3]):
        print(k)