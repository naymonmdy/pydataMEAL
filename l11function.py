
#Functions (def)
    #1.Simple Function with no parameter
    #2.Function with Parameter
        #1.Single Parameter Function
        #2.Multi Parameter Function
    #3.Function with a Return Value
    #4.Function with multi Return Value
    #5.Function with Default Parameter 
    #6.Lambda Function (Anonymous Function )
    #7.Generator Function


#1.Simple Function with no parameter
def sayname():
    print("Hello Aung Aung")
#call function
sayname()

#2.Function with Parameter
     #1.Single Parameter Function
def saycity(city):
    print("Hello " + city )

saycity("Mandalay")
saycity("Yangon")


#3.Function with default Parameter
def country(country ="Thailand"):# Default Parameter
    print("Hello "+country)

country('Myanmar')
country()


#4.Function with Return Value
def sayage():
    return "I am 25 year old"

print(sayage())


def saynickname():
    result ="Daw Pu"
    return result
print(saynickname())

def saynum(num1=20):
    return num1
print(saynum(100))
print (saynum())


def greeting (value = "Yamin"):
    return f"Hello {value} "
print(greeting("Su Su"))

print(greeting())


def funone(num1,num2):
    result = num1+num2
    return result

print(funone(10,20))


def funtwo(num1,num2=200):
    result = num1+num2
    return f"total value is = {result}"

print(funtwo(10))
print(funtwo(20,30))

#5.Function with multi Return Value

def saynameandage():
    name = "Honey"
    age = 32
    return name,age

print(saynameandage())
name,age = saynameandage()#FIFO and first in first out
print (name)
print (age)

#6.Lambda Function (Anonymous Function )

addresult = lambda num1,num2,num3:num1+num2+num3 #single line Lambda line
print(addresult(300,200,400))


#6.Lambda Function with default parameter (Anonymous Function )

sumresult = lambda num1,num2=200,num3=500:num1+num2+num3 #single line Lambda line
print(sumresult(700))
print(sumresult(50,100))
print(sumresult(400))


firstname = input("Enter first name = ")
lastname = input("Enter last name = ")

# fullname ="Hello %s %s" %(firstname,lastname)
fullname = f"Hello {firstname} {lastname}"
print(fullname)



# Generator Function

def  genfun():
    yield 1
    yield 2
    yield 3

print(genfun()) #<generator object genfun at 0x100974930>
print(list(genfun())) #[1, 2, 3]

for value in genfun():
    print(value) #1  2  3


print ("Hello Sir")

