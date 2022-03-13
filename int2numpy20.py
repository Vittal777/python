from numpy import *
arr = array([45,65,78,90,12,37,89,6])
fil_arr = []
for i in arr:
    if i % 2 == 0:
        fil_arr.append(True)
    else:
        fil_arr.append(False)
ar = arr[fil_arr]
print(fil_arr)
print(ar,'\n')
# Other methods : Creating filter directly from array
arr1 = array([40,31,59,108,42,90,11,101])
fil_arr1 = arr1 > 50
ar1 = arr1[fil_arr1]
print(fil_arr1)
print(ar1,'\n')
arr2 = array([50,31,45,68,90,32,15,102])
fil_arr2 = arr2 % 2 == 0
ar2 = arr2[fil_arr2]
print(fil_arr2)
print(ar2)