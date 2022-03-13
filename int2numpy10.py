# Another method of iterating 2D array
from numpy import *
arr = ([[3,7,8],[5,9,0]])
for i in arr:
    for j in i:
        print(j)
# Another method of iterating 3D array
print('\n')
arr1 = array([[[3,6,9],[1,4,7]],[[4,2,3],[7,0,5]]])
for a in arr1:
    for b in a:
        for c in b:
            print(c)
# Iterations using nditer()
print('\n')
arr2 = array([[[3,4,5],[4,0,9]],[[1,5,7],[3,2,1]]])
for i in nditer(arr2):
    print(i)