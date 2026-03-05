
import numpy as np


arr = np.array([[1,2,3,4],[4,56,5,7]])
print(arr)
print(type(arr))
print(arr.ndim)

import time
python_list1 = list(range(100000))
python_list2 = list(range(100000))


np_array1 = np.arange(100000)
np_array2 = np.arange(100000)


# Performance Comparison with Numpy and Lis

start_time = time.time()
result = [python_list1[i]+python_list2[i] for i in range(len(python_list1))]

end_time = time.time()
total_time_arr= end_time - start_time
print (f"Total time for list operation : {total_time_arr:.6f} seconds")

start_time = time.time()
result = np_array1+np_array2
end_time = time.time()
total_time_arr = end_time - start_time
print (f"Total time for numpy array operation : {total_time_arr:.6f} seconds")


# To create array with numpy
A = np.ones((3,3))
B = np.eye(2,2)
C = np.zeros((2,2))
D = np.diag((-2,-3))

print(A)
print(B)
print(C)
print(D)

print(A.ndim)
print(B.ndim)
print(C.ndim)
print(D.ndim)


#Numpy 2D Array Indexing
# -1 to get last value
arr4 = np.array([[1,2,3,4],[4,56,5,7]])
print(arr4[1,-1])


arr4_transpose = np.transpose(arr4)
print(arr4_transpose)


#Numpy 1D Array Slicing
#arr[start:end:step]
#arr[4:] => 4 to end
#arr[:4] => start to 3
#arr[-3,-1] => from last to 2
#arr[1:4:2] => 1 to 3 with step 2
#arr[::2] => all value with step 2
#arr[::-1] => to convert form last to first



#Numpy Data Types
# i = integer
# b = boolean
# u = unsigned integer
# f = float
# c = complex
# m = timedelta
# M = datetime
# O = object
# S = String 
# U = unicode String 
# V = void type

print(arr4.dtype) #int64

arr5 = np.array(["melon","banana","stawberry"],dtype="S")
print(arr5.dtype)


arr6 = np.array([1,2,4],dtype="S")
print(arr6.dtype)

#To convert data type
arr6 =arr6.astype("i")
print(arr6)
print(arr6.dtype)

arr6 =arr6.astype(bool)
print(arr6)
print(arr6.dtype)


arr5 =arr5.astype(bool)
print(arr5)
print(arr5.dtype)