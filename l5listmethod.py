names = ['aung aung','su su','yu yu','nandar']
print(names)

mixeds =[1500,"hello",123.4,True,"World",False]
print(mixeds[0])
print(mixeds[3])
print(mixeds[-1])
print(mixeds[-3])


print(mixeds[0:1]) #1500
print(mixeds[0:2]) #1500,hello
print(mixeds[1:3]) #hello,123.4
print(mixeds[0:3]) #1500,hello,123.4,True,World,False

# Start:end:step
print(mixeds[0:6:2]) #1500,123.6,World
print(mixeds[0:6:3]) #1500,True

# Copy Array
mix2=mixeds #all
mix2=mixeds[:] #all
mix2=mixeds[0:4] #1500,hello,123.4,True
mix2=mixeds[::-1] #reverse Copy =>False,World,True,123.4,hello,1500

getlength =len(names)
print(getlength) #5


colors = ["red","green","blue"]
print(colors)

colors[0]="pink"
print(colors) #[]'pink', 'green', 'blue']

colors.append("white") #must be sigle value ['pink', 'green', 'blue', 'white']
print(colors)

#add data from end multi 
colors.extend(["gold","black","violet"])
print(colors)


#insert(index,value)
colors.insert(0,"steelblue")
print(colors)


#remove with value
colors.remove("white")


#remove end value
colors.pop()


#remove  value and index
del colors[1]
del colors[1:3]
print(colors) #['steelblue', 'gold', 'black']

vals =[1,2,3,4,5]
print(f"Before clear values{vals}") #Before clear values[1, 2, 3, 4, 5]
vals.clear()
print(f"After clear values{vals}") #Empty array


boys = ["aung aung","zaw zaw","kyaw kyaw","hein min","yae lay","min khant"]
boys.sort()
print(boys)

boys.reverse() # reverse array 

ages = [16,25,25,18,44,2,3,21,18,30,12,18]
countof18 = ages.count(18)
countof25 = ages.count(25)
print(countof18)
print(countof25)
print(ages.index(25))
print(ages.index(30))

#nested list

numbers =[[1,2,3],[21,3,4,21],[234,2,1,23]]
print(len(numbers))
print(numbers[0])
print(numbers[1][2])
print(numbers[2][0])


greeting =["Hello" ,"Su Su"]
print(" ".join(greeting))
print("-".join(greeting))

# 
val1,val2=greeting
print(val1)
print(val2)