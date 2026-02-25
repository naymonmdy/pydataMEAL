num1 = 256.99
print(int(num1))


num2 = "255"
print(int(num2))

# num3 = "255.3"
# print(int(num3))
# ValueError: invalid literal for int() with base 10: '255.3'

num4 = -256.99
print(int(num4))
print(abs(num4))


num5 = "254.99"
print(float(num5))
print(type(num5))


num6 = 2234.35631
print(round(num6))
print(round(num6,2))


print(pow(2,3))
print(divmod(10,3)) #3,1 divide and modulus
print(divmod(10,2)) # 5,2 divide and modulus

print(max(12,1,2,3124,1,121)) #3121
print(min(12,1,2,3124,1,121)) #1
print(sum([1,2,3,4,5])) #15
print(sum((1,2,3,4,5))) #15



#Mathematical Functions
#to use import 

import math
print(math.ceil(32.21))
print(math.floor(32.21))
print(math.pow(2,3))
print(math.sqrt(16))
print(math.sqrt(35))#5.916079783099616



# default e
print(math.e) #2.718281828459045 euler number is approximately
print(math.pi) #3.141592653589793 
print(math.log(100,10)) #2.0 (log base 10)
print(math.log(81,9)) #2.0 (log base 9)
print(math.log(100)) #4.60517018598809 (log base e)

print(math.log10(100)) #2.0 (log base 10)
print(math.log10(1000)) #3.0 (log base 10)
print(math.log2(8)) #3.0 (log base 2)

#Exponential and default base is e
print(math.exp(2))


import random
print(random.random())
print(random.random())


# random inter
print(random.randint(1,10))
print(random.uniform(1.0,10.0))

numlist = [101,2,3,20,234,32,90]
print(random.choice(numlist))


numtup = (101,2,3,20,234,32,90)
print(random.choice(numtup))