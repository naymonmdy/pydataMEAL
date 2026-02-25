
#Comparison Operator
    # == Equal
    # != Not Equal
    # > Greater
    # < Less Than
    # >= Greater Than or Equal To 
    # <= Less Than or Equal To 
    # is,is not Identity Operators
    # in,not in Membership Operators


#Functions (def)
    #1.Simple Function with no parameter
    #2.Function with Parameter
        #1.Single Parameter Function
        #2.Multi Parameter Function
    #3.Function with a Return Value
    #4.Function with multi Return Value
    #5.Function with Default Parameter 
    #6.Lambda Function (Anonymous Function )


def sayname():
    print("Hello Aung Aung")




if True:
    print("Yes")
else:
    print("No")


if False:
    print("Yes")
else:
    print("No")

if 5 == 5:
    print("Equal")
else:
    print("Not equal")


a = [10,20,30]
b = a
c = [1000,2000,300]

print (a is b)
print (a is c)
print (a is not c)

x = [10,20,30,40,50]

print (20 in x)
print ("e" in 'student')
print ("o" not in 'orange')

girls = ["su su","mu mu",'yu yu']
print ("su su" in girls) # Case Sensitive


# => isinstance(val,type)
if isinstance("hello",str):
    print("yes")
else:
    print("No")

if isinstance(78,str):
    print("yes")
else:
    print("No")

if isinstance(78.5,float):
    print("yes")
else:
    print("No")

if isinstance(False,bool):
    print("yes")
else:
    print("No")

if isinstance(girls,list):
    print("List")
else:
    print("No List")


print(type({ "name" :"su su"})) #<class 'dict'>

if isinstance({ "name" :"su su"},dict):
    print("Dict")
else:
    print("No Dist")

#call function
sayname()


# nested if statement

initnum =10


if initnum>10:
    print("positive")
else:
    print("negative")



