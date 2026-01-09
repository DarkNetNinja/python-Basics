#List

courses = ['ba','bcom','bsc','ma','mcom','msc']
print(courses)
print(type(courses))

print(courses[0])
print(courses[3])
print(courses[0:5])
print(courses[-1])

#list Functions(list allows duplicates)
courses.append("BE") #use to append the element at last
print(courses)

courses.insert(3,"BTech") #insert an element somewhere in middle(requires position and value)
print(courses)

c="B.Pharma"
courses.append(c) #we can append another variable as well
print(courses)

list = ['11th','12th']
courses.append(list) #we can append a list within list
print(courses)
print(courses[-1])

courses.extend(list) #extend list by appending elements from iterable
#extend actually unpack the other list and adds items to the original list instead of creating of nested list
print(courses)#now the new list inserted not as a list,but as a seperate elements

courses.pop()
print(courses) #To remove last element of list 

courses.remove("11th")
print(courses) #to remove a specific item use remove

#python sort based on ASCII character not just standard alphabet
# Uppercase letters (A-Z) have lower codes (65-90).
# Lowercase letters (a-z) have higher codes (97-122).

fruits = ['mango','banana','chickoo','watermelon','pineapple']
print(fruits)

fruits.sort()
print(fruits)

fruits.reverse()
print(fruits)

print(fruits)

nums = [12,4,45,1,100,2]
print(nums)
nums.sort()
print(nums)

print(len(nums))
print(len(fruits))
print(len(courses))

print(max(nums))
print(min(nums))
print(sum(nums))

print(max(fruits)) #Returns the one with highest alphabet, when list is made of strings
print(min(fruits))

#iterating list
# iterate means repeat,when we say iterating a list in python we mean going 
# through list items one by one

for fruit in fruits:
    print(fruit)
    print("I am inside the loop")

for fruit in fruits:
    print(f"{fruit} {len(fruit)}")

for fruit in fruits:
    print(f"{fruit} {fruit.upper()} {len(fruit)}")

#enumerate

for id,fruit in enumerate(fruits): #enumerate returns index along with actual item hence we need to catch it explicitly
    print(id,fruit)

cubes = []
for i in range(5):
    i **= 3
    cubes.append(i)
print(cubes)

#Nested list
fruits = [['mango','banana','chickoo'],['watermelon','pineapple']]
print(fruits)
print(len(fruits))
print(len(fruits[0]))
print(fruits[0],type(fruits[0]))
print(fruits[1],type(fruits[1]))
print(fruits[0][1])
print(fruits[1][1])