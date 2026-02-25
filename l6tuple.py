# tuple is same with list

#Difference of tuple and list
#1. TypeError: 'tuple' object does not support item assignment
#2. Mutable(change) and Immutable (not changeable)
#3. List :generally slower than tuple
#4. Usages 
    #  list :need to change , user lists, shopping carts
    #  tuple :fixed item , geograpic , settings, database records, assetes,
# 5. Methods : many built-in method for modifying list
# tuple can't CRUD 


# List
print(type([1,2,3,4]))


# Tuple
print(type((1,2,3,4)))

# Create with paranthesis
tuple1 = (11,12,3,4,5)
print(tuple1)


tuple2 = 1,2,3,4,54
print(tuple2)



print(tuple1[0])

# tuple1[1] =100
# TypeError: 'tuple' object does not support item assignment

print(tuple1.count(11))
print(tuple1.index(3))

#Tuple unpacking

students = ("aung aung","mg mg", "su su")
boy,boy2,girl =students

print(boy2)
print(boy)
print(girl)
