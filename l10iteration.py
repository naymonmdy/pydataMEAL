# For In loop
# Iteration a list


colors = ["red","green","blue"]

for color in colors:
    print(color)


message = "Hello World"
print(len(message)) #11

for msg in message:
    print(msg)


# Iteration a Dist

student = {"name":"su su","age":20,"city":"Mandalay"}

print(student.items())  #dict_items([('name', 'su su'), ('age', 20), ('city', 'Mandalay')])


for key in student:
    print(key,student[key])

for key,value in student.items():
    print(key,"=",value)


#range() in for in loop
    
for x in range(10):
    print(x)  #0 to 9

print(f"outside value is {x}")


for y in range(1,5):
    print(y)  #1 to 5

print(f"outside value is {y}")


for z in range(1,10,2):
    print(z) #1 3 5 7 9 

print(f"outside value is {z}") 


#break and containue
    
for i in range(10):
    if i==5:
        break
    print(i)

print(f"outside value is {i}") 


for q in range(10):
    if q==5:
        continue
    print(q)

print(f"outside value is {q}") 


for j in range(10):
    if j%2==0:
        continue
    print(j)

print(f"outside value is {j}") 


#nested loop

staffs = [
    ["aung aung","kyaw kyaw","zaw zaw"],
    ["nu nu","yu yu","su su"],
    ["thidar","mu yar","nilar"]
]

# for staff in staffs:
#     for people in staff:
#         print(people)

# for staff in staffs:
#     for people in staff:
#         print(people)
#     print()

for staff in staffs:
    for people in staff:
        print(people,end=" ")
    print()
        

#While loop

idx = 0


while idx < 10:
    print(f"Index : {idx}")
    idx +=1

print(f"Outside value is {idx}")




count = 0


while count < 10:
    print(f"count : {count}")
    count +=1

print(f"Outside value is {count}")




paints = ["red","green","blue"]
print(enumerate(paints))


for idx,paint in enumerate(paints):
    print(idx,paint)


index = 0

while index < len(paints):
    print(index,paints[index])
    index += 1