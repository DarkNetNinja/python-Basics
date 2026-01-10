#dictionary

#stores data as a key value pair
#is a collection,ordered,changable and does not allow duplicate,written with curly braces and have key and values

company = {
    "name":"Tesla",
    "founder":"Elon Musk",
    "established": 2003
}
print(company) #key must be string and values can be of any datatype

print(type(company))

print(company["name"]) #To access specific dictionry items
print(len(company)) #length of dictionary

#To change value of an item
company["name"] = "TESLA"
print(company)

#add new item to dictionary
company["location"] = "US"
print(company)

#Dictionary Functions

Dict = {
    "name":"Anurag",
    "Rollno":34,
    "city":"Jalgaon",
    "Degree":"Engineering"
}

#another way to get items
print(Dict.get("name"))
print(Dict.get("namee")) #name is not defined so we get none

#key() and value() Functions
print(Dict.keys())
print(Dict.values())
print(Dict.items())

Dict["newkey"] = "newvalue"
print(Dict.keys())
print(Dict.values())

#To delete an item use pop
Dict.pop("Degree") #use pop function and pass key
print(Dict)

Dict = {
    "name":"Anurag",
    "Rollno":34,
    "city":"Jalgaon",
    "Degree":"Engineering"
}
print(Dict)

del Dict["Degree"] #syntax -> del dict_name['key']
print(Dict)

print(company)
company.clear()
print(company)

#Dictionary Looping

new = dict({'name': 'Apple', 'year': 1975, 'founder': 'Steve Jobs and Steve Wozniak'})     # dict is special keyword, wrap your dictionary within dict() 
print(new)
print(type(new))

for item in new: #only prints keys
    print(item)

for item in new:
    print(item,new[item])

for key,values in new.items():
    print(key,values)

for key in new.keys():
    print(key)

for value in new.values():
    print(value)

#sort the dictionary
for key in sorted(new):
    print(key)

#nested Dictionary
company = {
    'name': 'Apple',
    'year': 1975,
    'founders': {
        'first': 'Steve Jobs',
        'second': 'Steve Wozniak'
    }
    }
print(company)
print(company["founders"])
print(company["founders"]["first"])

for key,value in company.items():
    print(key,value)

print(type(company["founders"]))