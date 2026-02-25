# => Data Containters

# list
mylist = [1,2,3,4,5]
print(type(mylist)) #<class 'list'>

#tuple
mytuple = (1,2,3,4,5)
print(type(mytuple)) #<class 'tuple'>



#dict
mydict = {"a":1,"b":2,"c":3}
print(type(mydict)) #<class 'dict'>



#set
myset = {1,2,3,4,5}
print(type(myset)) #<class 'set'>


dict1 = {}
print(type(dict1)) #<class 'dict'>


set1 = {}
print(type(set1)) #<class 'dict'>  and not get set

# create an empty set 
set2 = set()
print(type(set2)) #<class 'set'>


colors = {"red","orange","blue","white","black","green"}
print(colors)
print(type(colors)) #set

for color in colors:
    print(color)

print("green" in colors)
print("steelblue" in colors)



#Adding a single Element
fruits ={'apple','orange'}
print(fruits)


fruits.add("cherry")
print(fruits) #{'apple', 'cherry', 'orange'}



#Adding a multiple Element
# fruits.add("guava","coconut")
# print(fruits) #error

fruits.update(["guava","coconut"])
print(fruits) #


#Remove a single Element
fruits.remove("apple")
print(fruits)

# fruits.remove("banana")
# print(fruits) # error if not exit


#Removing Elements (using discard())
fruits.discard("banana")
print(fruits) # if no element , no error


#Remove Elements
fruits.clear()
print(fruits) #set()

#Frozenset (Immutable version of set)
fornumbers = frozenset([10,20,30,40,50])
# fornumbers.add(50)
print(fornumbers) #not add in frozenset

# fornumbers.remove(50)
print(fornumbers) #not remove in frozenset

print(30 in fornumbers)
print(60 in fornumbers)


set3 = {2,3,4,5,6}
set4 = {4,5,6,7,8,9}

#Union Combines (|) Override for same elements
print(set3 | set4)

#Intersection Combines (&) get same element
print(set3 & set4)

#Difference Combines (-) get difference element from the left
print(set3 - set4) #{2, 3}
print(set3.difference(set4)) #{2, 3}

print(set4 - set3) #{8, 9, 7}
print(set4.difference(set3)) #{8, 9, 7}

# Symmetric Difference (^) get all difference
print(set3^set4)#{2, 3, 7, 8, 9}
print(set3.symmetric_difference(set4))#{2, 3, 7, 8, 9}

# => Set Comprehension
# {expression for item in iterable condition}

squares = {x**2 for x in range(4)}
print(squares)

# 0  ** 2 = 0 
# 1  ** 2 = 1  
# 2  ** 2 = 4 
# 3  ** 2 = 9 
# 4  ** 2 = 16 

evens = {x for x in range(10) if x%2==0}
print(evens) #{0, 2, 4, 6, 8}

uniqchars = {char for char in "Hello world"}
print(uniqchars) #{'d', 'w', 'e', ' ', 'l', 'o', 'r', 'H'}

numbers = [1,2,2,3,4,7,5,7]
uniqnumbers = {char for char in numbers}
print(uniqnumbers) #{1, 2, 3, 4, 5, 7}


# Nested loops in set comprehension
                            # 0 to 2            0 to 1
couplenums = {(x,y) for x in range(3) for y in range(2)}
print(couplenums) #{(0, 1), (2, 1), (0, 0), (1, 1), (2, 0), (1, 0)}



# Generator Function


