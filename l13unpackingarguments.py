#=> Unpacking Arguments

def sayhi(name,age):
    print(f"Hello friend! my name is {name} and i am {age} year old")

sayhi("testing",32) #Hello friend! my name is testing and i am 32 year old

args = ("Nay Mon",31)
sayhi(*args)#Hello friend! my name is Nay Mon and i am 31 year old


def addingnumbers(a,b,c):
    print(f"Total result is = {a+b+c}")

total = (10,20,30)
addingnumbers(*total) #unpack tupel into argument

total =[10,20,20]
addingnumbers(*total) #unpack list into argument

listinfo = {"name":"Hla Hla","age" :34} #unpack dist into argument
sayhi(**listinfo)


