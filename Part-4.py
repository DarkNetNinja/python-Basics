#Tuple 
# Tuple is one of the four built-in collection datatypes
#ordered and unchangable(immutable),Duplicates are allowed,written in round bracket

courses = ('ba','bcom','msc')
print(courses)
print(type(courses))

print(courses[1])
print(courses[2])

print(courses.count('ba'))
print(courses.count('baa'))

print(courses.index('msc'))

courses = ('ba','bcom','msc','ba','bcom')

print(courses.count('ba'))
print(courses.index('msc'))

for course in courses:
    print(course)


for id,course in enumerate(courses):
    print(id,course)

print(len(courses))

nums = (1,4,3,5)
print(type(nums))

#mix of str and int and bool is allowed in tuple

data = ('ba',3,True,'bsc')
print(data)
print(type(data))
print(type(data[0]))
print(type(data[1]))
print(type(data[2]))

#lets do the same with for loop
for item in data:
    print(item,type(item))

new = ('50')
print(type(new))

new = ('50',)
print(type(new))

#Concat two tuples

print(('a','b','c') + (1,2,3))

new = ('50',)
new1 = ('apple',)
new2 = ('mango','orange')
print(new + new1+ new2)

#to delete use del
del new2
#print(new2)


#check whether an element is in Tuple
fruits = ('apple','mango')
print('mango' in fruits)
print('Mangoes' in fruits)

print(max(3,5,6,7))
print(min(5,7,3,4))


num = [1,3,4,5]
num = tuple(num)
print(num)

num1= (1,2,3,4,5,6)
print(num1[-1])
print(num1[-2])

courses = ('ba', 'bcom', 'bsc', 'be', 'ma', 'mcom',' msc', 'me')
print(courses[:5])
print(courses[1:5])
print(courses[-3:])