#Copy and view array 
import numpy as np
arr = [1,2,3,5,6]
x = arr.copy()
x[0]=43

arr = np.array(arr)
x = np.array(arr)

print(arr)
print(x)
print(arr.dtype)


y=arr.view()
y[2] = 35
print(y)
print(arr)


# Get the shape of an array 
sh = np.array([[1,2,4,6,5],[4,5,6,7,45]])
print(sh.shape)


# Reshape the dimension of array
sh = sh.reshape(2,5)
print(sh)


#Flattening the array to one D array
print(sh.reshape(-1))

#Looping of iteration the array
sh1 = np.array([[1,2,4,6,5],[4,5,6,7,45]])

for x in sh1:
    for y in x:
        print(y)
        
#loop with nditer function to array
for x in np.nditer(sh1):
    print(x)
    
for x in np.ndenumerate(sh1):
    print(x)
    
print("....................................................................")

#combining the array  with concatenate function axis ,0,1,2
arr1 = np.array([[1,3,8,6],[2,3,54,6]])
arr2 = np.array([[4,56,8,8],[3,3,4,5]])

print(np.concatenate((arr1,arr2)))
print(np.concatenate((arr1,arr2),axis=1))


print("....................................................................")


#combining the array with stack to get new dimension
print(np.stack((arr1,arr2)))


#filter array

a = np.array([3,4,56,7,7,75,33,22])

filter_array=[]


for val in a:
    if val > 32:
        filter_array.append(True)
    else:
        filter_array.append(False)
        

result = a[filter_array]
print(filter_array)
print(result)


div2_array = []
for val in a:
    if val%2 ==0:
        div2_array.append(True)
    else:
        div2_array.append(False)
        
div2 = a[div2_array]
print(div2)


#advance filtering 
notdiv2 = a[a%2!=0]
print(notdiv2)


div4 = a[a%4==0]
print(div4)


from numpy import random
x = random.randint(30) # get integer
x = random.rand() # get float from 0 to 1
# print(x)


rand_num = random.randint(100,size=(3,6))
print(rand_num)

#random Sampling
rand_num2 = random.choice([2,4,7,8,66,7],size=(3,5))
print(rand_num2)


#random Sampling with probability ,total p =1
rand_num3 = random.choice([2,4,7,8],p=[0.3,0.4,0.2,0.1],size=(100))
print(rand_num3)

#random permutation(not change origin array) and shuffle( can change origin array)
rand_num4 =np.array([3,5,7,3,2,89,3])
print(random.permutation(rand_num4))
print(random.shuffle(rand_num4))

#normal distribution

rand_num5 = random.normal(size=20)
print(rand_num5)