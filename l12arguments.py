# Detail Function
# Type of Argument in Python

# Positional Arguments
# Keyword Arguments
# Default Arguments
# Variable-length Arguments (*args) (Non-Keyword Variable Arguments)
# Variable-length Arguments (**kwargs Keyword Variable Arguments)

# Positional Arguments
def greet(name,age):
    print(f"Hello friend . My name is {name}, and i am {age} years old.")

greet("Su Su",30) #Hello friend . My name is Su Su, and i am 30 years old.
greet(30,"Nay Nay") #Hello friend . My name is 30, and i am Nay Nay years old.

# Keyword Arguments
def hifi(name,age):
    print(f"Hello friend . My name is {name}, and i am {age} years old.")

hifi(name="mu mu",age=30) #Hello friend . My name is mu mu, and i am 30 years old.
hifi(age=30,name="mu mu") #Hello friend . My name is mu mu, and i am 30 years old.

# Default Arguments
def hime(name,age=18):
    print(f"Hello friend . My name is {name}, and i am {age} years old.")

hime("Yamin") #Hello friend . My name is Yamin, and i am 18 years old.
hime("Thuzar",30) #Hello friend . My name is Thuzar, and i am 30 years old.


# Variable-length Arguments (*args) (Non-Keyword Variable Arguments)
def boys(*args):
    print(args)

boys("aung aung") #('aung aung',)
boys("aung aung","kyaw kyaw") #('aung aung','kyaw kyaw')
boys("aung aung","kyaw kyaw","zaw zaw","tun tun") #('aung aung', 'kyaw kyaw', 'zaw zaw', 'tun tun')
#boys("aung aung",args="kyaw kyaw") #error when including keywords Arguments

# Variable-length Arguments (**kwargs Keyword Variable Arguments)
def sumresults(*numbers):
    total = sum (numbers)
    print(f"Sum result number is {total}")

sumresults(1,2,3)  #Sum result is =6
sumresults(10,20,30)  #Sum result is =60

def myfunone(num,*nums):
    print(num) #1
    total=sum(nums)
    print(total) #14
myfunone(1,2,3,4,5)

# Variable-length Arguments (**kwargs Keyword Variable Arguments)
def personinfos(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}={value}")

personinfos(name="nay mon",age=31,gender="M")
personinfos(job="MEAL officer")


#Exercises (Combining Different types of Argument)
def emailsender(address,*messages,**files):
    print(f"Address = {address}")
    if messages:
        for message in messages:
            print(f"Message = {message}")
    if files:
        for key,value in files.items():
            print(f"{key} = {value}")

#emailsender("naymon2021@gmail.com","Hello admin","I want to request video file",lesson="Python B1",date="22-02,2024")
emailsender("naymon2021@gmail.com")


def studentinfos(name,age=18,*hobbies,**infos):
    print(f"Name = {name}")
    print(f"age = {age}")
    if hobbies:
        for hobbie in hobbies:
            print(f"hobbie = {hobbie}")
    if infos:
        for key,value in infos.items():
            print(f"{key}= {value}")

studentinfos("nay nay", 31,'drawing','coding','playing guitar',city="Mandalay",job="data analyst")


def staffinfos(name,age=18,*hobbies,**infos):
    print(f"Name = {name}")
    print(f"age = {age}")
    if hobbies:
            print(f"Hobbies = {hobbies}")
            print(f"Hobbies = {','.join(hobbies)}")
    if infos:
        for key,value in infos.items():
            print(f"{key}= {value}")

staffinfos("mon mon", 31,'baby caring','tarvelling',city="Mandalay",job="data analyst")