
#
lady = {"name":"Yadanar","age":30}

print(lady)

#get Method
print(lady.get("name")) #Yadanar
print(lady.get("gender")) #None
print(lady.get("gender","Not Defined")) #Not Defined

#keys and values Methods with looping with list
print(lady.keys()) #dict_keys(['name', 'age'])
print(list(lady.keys())) #['name', 'age']
print(list(lady.keys())[0]) #'name'
print(list(lady.keys())[1]) #'age'


print(lady.values()) #dict_values(['Yadanar', '30'])
print(list(lady.values())) #['Yadanar', '30']
print(list(lady.values())[0]) #Yadanar
print(list(lady.values())[1]) #30



#items Method to key and value add in tuple
print(lady.items()) #dict_items([('name', 'Yadanar'), ('age', 30)])
print(list(lady.items()))#[('name', 'Yadanar'), ('age', 30)]
print(list(lady.items())[0])#('name', 'Yadanar')
print(list(lady.items())[1])#('age', '30')
print(list(lady.items())[0][0])#('name'')
print(list(lady.items())[0][1])#('Yadanar')


#update Method
lady.update({'age':20,"gender":"female"})
print(lady)


#pop Method or remove or clear and pop function need al least one parameter in dist or object
lady.pop('age')
print(lady)

#all clear data
lady.clear()
print(lady)


#popitem not effet in original value  and get last value
girl ={"name":"Yadanar","age":30,"city":"Mawlamyine"}

item = girl.popitem() #('city', 'Mawlamyine') as tuple
print(item) #('city', 'Mawlamyine') as tuple
print(item[0]) #('city')
print(item[1]) #('Mawlamyine')


#copy or clone
woman =girl
woman =girl.copy()
print(woman)
#
#
#
#