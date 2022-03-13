# NumPy using random
# randint generates a random integer
from numpy import *
r = random.randint(50)
print(r,'\n')
# rand() method returns a random float between 0 and 1
r1 = random.rand()
print(r1,'\n')
# randint() method takes a size parameter where you can specify the shape of an array.
r2 = random.randint(75,size = (7))
print(r2,'\n')
r3 = random.randint(50,size=(3,7)) # 2D array with 3 rows and 7 elements each.
print(r3,'\n')
# rand() also allows to specify the shape
r4 = random.rand(5) # array with five random float integers b/w 0 and 1
print(r4,'\n')
r5 = random.rand(3,6) # array with 3 rows and 6 elements each in it
print(r5)