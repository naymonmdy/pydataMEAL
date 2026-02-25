name = "aung kyaw"
print(name)
print(name[1])#u
print(name[3])#g
print(name[0])#a
print(name[-2])#a
print(name[-1])#w

#start:end:step
print(name[0:1])#a
print(name[0:2])#au
print(name[0:3])#aun
print(name[0:4])#aung

print(name[1:4])#ung
print(name[1:7])#ung ky
print(name[0:4])#aung
print(name[0:9])#aung kyaw

print(name[0:9:1]) #aung kyaw
print(name[0:9:2]) #an yw
print(name[0:9:3]) # agy

fullname = name #aung kyaw
fullname = name[:] #aung kyaw
fullname = name[0:4] #aung
fullname = name[::-1] #wayk gnua
print(fullname)

getlength = len(name) 
print(getlength) #9

text ="hello friend"
print(text.upper()) # HELLO FRIEND
print(text.capitalize()) # Hello friend
print(text.title()) # Hello Friend


task = "HAVE TO GO"
print(task.lower()) # have to go
print(task.casefold()) #have to go


todo ="Have To Shop"
print(todo.swapcase()) #hAVE tO sHOP


hifi = "   hello friend  "
print(hifi.strip()) #hello friend
print(hifi.lstrip()) #hello friend
print(hifi.rstrip()) #   hello friend

#case sensitive
greet = "Hello friend"
print(greet.replace("friend","sir")) # Hello sir
print(greet.replace("Friend","sir")) # Hello friend

print(greet.startswith("H")) #Ture
print(greet.startswith("h")) #False


#case sensitive
print(greet.endswith("nd")) #Ture
print(greet.endswith("End")) #False


mobile ="OPPO"
print(mobile.isupper())#True
print(mobile.islower())#False

num1=528
num2="1500"
num3="ten"
num4="number ten"
num5="Hay!"


#AttributeError: 'int' object has no attribute 'isdigit
#print(num1.isdigit())
print(str(num1).isdigit())#True
print(num2.isdigit())#True
print(num3.isdigit())#False


print(num2.isalpha())#False
print(num3.isalpha())#True


print(num2.isnumeric())#Ture
print(num3.isnumeric())#False

print(num2.isalnum())#True
print(num3.isalnum())#True
print(num4.isalnum())#False bz space
print(num5.isalnum())#False bz !


middlename= " "
print(middlename.isspace()) #True


nickname="Aung Moe"
print(middlename.isspace()) #False
print(middlename.istitle()) #True

sayhi = "Hi my friend"
print(sayhi.split()) ##['Hi','My','Firend']


color ="red,green,blue"
print(color.rsplit()) ##['red,green,blue']

sayhello = "Hello\nfriend"
print(sayhello.splitlines()) ##['Hello','Firend']

sayhifi = "hello friend Mr.Mg"
print(sayhifi.partition(" ")) ##('Hello',' ','Friend Mr.Mg')
print(sayhifi.partition(".")) ##('Hello Friend Mr','.','Mg')


post = "Read"
print(post.ljust(10,'-')) #Read------
print(post.rjust(10,'-')) #------Read
print(post.center(10,'-')) #---Read---


city="hello {}"
print(city.format("Mandalay")) #Hello Mandaly

country = "Hello {} {}"
print(country.format("Mandalay","Myanmar")) #Hello Mandalay Myanmar

#dictionary

student = {"name":"su su"}
sayname = "Dear , {name}"
print(sayname.format_map(student)) #Dear, su su

print ("Hello my {} . are you !".format("friend","Aung Aung"))


val1= "sister"
val2="Su Su"
print ("Hello my {} . are you{} !".format(val1,val2))

