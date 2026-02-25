#=> Data Collection ( Module Containers)
# =>Counter from collection module

from collections import Counter
getcounts = Counter("Hello World")
print(getcounts) #  Counter({'l': 3, 'o': 2, 'H': 1, 'e': 1, ' ': 1, 'W': 1, 'r': 1, 'd': 1})



# =>Queues from collection module
from collections import deque
qpersons = deque(["Su Su","Nu Nu","Yu Yu"])
qpersons.append("Tun Tun")  # add to right end
qpersons.appendleft("Sai Sai") # add to left end
# for person in qpersons:
#     print(person)

# Sai Sai
# Su Su
# Nu Nu
# Yu Yu
# Tun Tun
    
#Removing Element
qpersons.pop() #remove from right
qpersons.popleft() #remove from left

for person in qpersons:
    print(person)

# Su Su
# Nu Nu
# Yu Yu
    
# =>defaultdict from collection module

from collections import defaultdict
items = defaultdict(list)


items["fruits"].append("apple")
items["fruits"].append("mango")
items["fruits"].append("banana")
items["colors"].append("orange")

print(items["fruits"])
print(items["colors"])
print(items["candy"])




# Group Items
groups = defaultdict(list)
foods = [("fruit","apple"),("fruit","orange"),("vegetable","carrot"),("fruit","mango")]

for key,value in foods:
    groups[key].append(value)

print(groups) #defaultdict(<class 'list'>, {'fruit': ['apple', 'orange', 'mango'], 'vegetable': ['carrot']})




numitems = defaultdict(int)
print(numitems["val"]) #0
numitems["val"] +=1
print(numitems) #defaultdict(<class 'int'>, {'val': 1})
print(numitems["val"]) #1


#Counting Elements
colorcounts = defaultdict(int)
candycolors = ["red","green","blue","red","green","black"]

for candycolor in candycolors:
    colorcounts[candycolor] +=1 

print(colorcounts) #defaultdict(<class 'int'>, {'red': 2, 'green': 2, 'blue': 1, 'black': 1})


# OrderedDict (from collections module)
from collections import OrderedDict

myorders = OrderedDict()
myorders["num1"] = 100
myorders["num2"] = 200
myorders["num3"] = 300
myorders["num4"] = 400
myorders["num5"] = 500

print(myorders) #OrderedDict({'num1': 100, 'num2': 200, 'num3': 300, 'num4': 400, 'num5': 500})
print(myorders["num2"]) #200

#Reordering Item
myorders.move_to_end("num2")
print(myorders) #OrderedDict({'num1': 100, 'num3': 300, 'num4': 400, 'num5': 500, 'num2': 200})

#overriding
myorders["num1"] =10
print(myorders) #OrderedDict({'num1': 10, 'num3': 300, 'num4': 400, 'num5': 500, 'num2': 200})

#Delete Item
del myorders["num3"]
print(myorders) #({'num1': 10, 'num4': 400, 'num5': 500, 'num2': 200})

config = OrderedDict()
config["host"] = "local host"
config["port"] = 8080
config["debug"] = True


for key,value in config.items():
    print(f"{key} : {value}")

#host : local host
# port : 8080
# debug : True
    

#NamedTuple (from collections module)

from collections import namedtuple
LuckyNumbers = namedtuple("Luckyname",["num1","num2","num3"])

getnum = LuckyNumbers(33,66,99)
print(getnum.num1)