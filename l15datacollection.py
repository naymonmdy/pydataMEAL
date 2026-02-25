

#Group Items

from collections import defaultdict
from collections import Counter

groups = defaultdict(list)
foods = [("fruit","apple"),("fruit","orange"),("vegetable","carrot"),("fruit","mango")]

for key,value in foods:
    groups[key].append(value)

print(groups) #defaultdict(<class 'list'>, {'fruit': ['apple', 'orange', 'mango'], 'vegetable': ['carrot']})



numitems = defaultdict(int)
print(numitems["val"]) #0
numitems["val"]=1 
print(numitems["val"]) #1


#Counting Element
colorcounts = defaultdict(int)
candycolors = ["red","green","blue","green","red","black","green"]

for candycolor in candycolors:
    colorcounts[candycolor] += 1

print(colorcounts) #defaultdict(<class 'int'>, {'red': 2, 'green': 3, 'blue': 1, 'black': 1})

#......................................................................................................................


# => OrderedDict (from collections module)
from collections import OrderedDict

myorders = OrderedDict()

myorders["num1"] = 100
myorders["num2"] = 200
myorders["num3"] = 300
myorders["num4"] = 400
myorders["num5"] = 500

print(myorders) #OrderedDict({'num1': 100, 'num2': 200, 'num3': 300, 'num4': 400, 'num5': 500})

#Reordering Item
myorders.move_to_end("num2")
print(myorders) #OrderedDict({'num1': 100, 'num3': 300, 'num4': 400, 'num5': 500, 'num2': 200})

#re-inserting
myorders["num1"] = 10
print(myorders) #OrderedDict({'num1': 10, 'num3': 300, 'num4': 400, 'num5': 500, 'num2': 200})

#Deleting Items
del myorders["num3"]
print(myorders) #OrderedDict({'num1': 10, 'num4': 400, 'num5': 500, 'num2': 200})



config = OrderedDict()
config['host']  = 'localhost'
config['port']  = 8080
config['debug']  =  True

for key,val in config.items():
    print(f"{key} : {val}")

#......................................................................................................................
# =>NamedTuple (from collection module)

from collections import namedtuple

LuckyNumbers = namedtuple("LuckyNumbers",["num1","num2","num3"])

getnums = LuckyNumbers(33,66,99)
print(getnums.num1) #33
print(getnums.num2) #66
print(getnums.num3) #99

#exercise with tuple , hard to remember what index number represents
staff = ("Yu Yu",20,"Developer")
print(staff[0]) #Yu Yu
print(staff[1]) #20
print(staff[2]) #Developer

#namedtuple
Student = namedtuple("Student",["name","age","profession"])
#pupil = Student("Su Su" ,30,"Engineer")
pupil = Student(name="Su Su" ,age=30,profession="Engineer")
print(pupil.name) # Su Su
print(pupil.age) # 30
print(pupil.profession) # Engineer

#......................................................................................................................
# =>ChainMap (from collection module)

from collections import ChainMap

dict1 = {"name" : "Aye Aye"}
dict2 = {"city" : "Mandalay"}
getdata =ChainMap(dict1,dict2)

print(getdata) #ChainMap({'name': 'Aye Aye'}, {'city': 'Mandalay'})
print(getdata["name"]) #Aye Aye
print(getdata["city"]) #Mandalay