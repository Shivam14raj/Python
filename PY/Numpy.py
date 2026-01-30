#NumPy= numerical python (pre made library)
import numpy as np

nums= np.array([1,2,3,4])
print(nums) 

from time import process_time 

# mylist= [i for i in range(10000)]

# start_time= process_time()

# mylist = [i+5 for i in mylist] 

# end_time= process_time() 

# print(end_time-start_time) 



# same for numpy array
# npnums= np.array([i for i in range(10000)])
# start_time= process_time()

# npnums+=5 

# end_time= process_time() 

# print(end_time-start_time)

# numpy is faster than list 


#----------------#
# 1D array using numpy
a= np.array([1,2,3])
print(a)
print(a.shape) #shape retuns a tuple 
# Shape: (3,)
# Meaning: 3 rows, 1 column

#2D array
b=np.array([[1], [2], [3]])
# [
#     [1],
#     [2],
#     [3]
# ] 
print(b.shape) # (3,1) 3 rows and 1 column

#per bracket= 1 dimension

c= np.array([[1,2], [3,4]])
print(c.shape) #(2,2) 

d= np.array([(1,2,3,4), (5,6,7,8)], dtype=float)
print(d)

# array of 0 
onlyZero= np.zeros((4,5)) # 4 rows and 5 column
print(onlyZero)

# array with 1 
onlyOnes= np.ones((2,2))
print(onlyOnes) 

#array of a particular value
z= np.full((5,6), 2)
print(z)

#identitiy matrix
idenMatrix= np.eye(5) # i need 4 rows and of 4 column
print(idenMatrix)

#random  values
randomVal= np.random.random((3,4)) # beyween 0 and 1 only 
print(randomVal)

# random values with int(soecific range)
randInt= np.random.randint(2,6, (4,5)) 
#(2,5): 2 is inclusive and 5 is execlusive 
print(randInt)

#evenly spaced values
evenly= np.linspace(10,20, 5) #(startpont, endpoint, noOfValues)
print(evenly)

# step value
e= np.arange(10,30,5) # 5-5 ke step pe values de de 
print(e)

#list to an numpy array
list2= [2,3,4]

numpyarray= np.asarray(list2)
print(numpyarray) 


# addition
f= np.random.randint(10,20, (3,3))
g= np.random.randint(10,20, (3,3))
print(f)
print(g)
print(f+g)  