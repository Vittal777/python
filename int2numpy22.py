# choice() method allows to genarate a random value based on array of values.
from numpy import *
arr = array([6,4,3,9,0,1])
c = random.choice(arr)
print(c,'\n')
c1 = random.choice(arr,size=(3,6))
print(c1,'\n')
'''
A random distribution is a set of random numbers that follow a certain probability density function.
Probability density is a function that describes continuous probability i.e., probability of all values in an array.
The probability is set b/w 0 and 1,where 0 indicates that the value never occur and 1 indicates that the value always occur.
The sum of all probability numbers should be 1.
'''
from numpy import *
c2 = random.choice([4,3,9,0,7],p=[0.5,0.2,0.1,0.2,0.0],size = (10)) #The sum of probabilities should be 1.
print(c2,'\n') # The value 7 will never occur, as it's probability is 0.0.
c3 = random.choice([4,9,0,1,2],p = [0.1,0.2,0.3,0.4,0.0],size=(3,4)) # No.of elements and p must be same
print(c3,'\n')
c4 = random.choice([4,9,0,1,2,7],p = [0.1,0.2,0.3,0.4,0.0],size=(3,4))