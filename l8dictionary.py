# Same with JSON 


# METHOD 1
student = {
    "name":"su su",
    "age":20,
    "city":"Yangon",

}

print(student)
print(student["name"])
print(student.get("name"))


# METHOD 2
staff = dict(name="Aung Aung",age=30,city="Mandalay")
print(staff)
print(staff["name"])
print(staff.get("name")) 


## in simple calling if key not exit , get Error
#.get()method if key not exit , result none


#can add field as default parameter
print(staff.get("country","myanmar")) 
print(staff.get("age",40))  #get 30


employee = {
    "name":"mg mg",
    "city":"Mandalay",
    "age":"39",
}

print(employee)

#to add data 
employee["email"] = "mgmg@gmail.com"
print(employee)

#override
employee["age"] = 40

#delete
del employee["city"]
print(employee)


worker = dict(name="nilar",age=28,city="Bago")


print(worker)