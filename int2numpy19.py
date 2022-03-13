# Getting some elements out of an existing array and creating a new array out of them,is called Filtering..
# done by using boolean list.If the value at an index is True that element is contained in the filtered way
# if the value at that index is False that element is excluded from the filtered array.
from numpy import *
arr1 = array(['Vittal','Raj','Sai','Kumar'])
arr = array([50,39,100,78])
i = [True,False,True,False]
ar = arr[i]
ar1 = arr1[i]
print(ar)
print(ar1)
# Creating a filter array
arr2 = array([36,49,101,19,167,89,12,95])
fil_arr = []
for i in arr2:
    if i>50:
        fil_arr.append(True)
    else:
        fil_arr.append(False)
ar2 = arr2[fil_arr]
print(fil_arr)
print(ar2)