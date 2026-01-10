#Set
#collection,unordered,unchangeable,and unindexed,do not allow duplicates

set0 = {"apple","banana","chickoo","apple","watermelon"}
print(set0)

#sets are unorder so you dont know in which order they will appear
# set items you cannot change but you can add or remove
#The value True and 1 are considered same values in set treated as set

print(len(set0)) #length of set

#set items can be of any datatype
set2 = {1,3,4,5,3}
set3 = {True,False,False}
set4 = {True,2,4,"apple"}

print(type(set0))
new = ("apple","banana","mango")
print(type(new))
set5 = set(("apple","banana","mango"))
print(set5)
print(type(set5))

#you cannot access the items in a set by referring by an index or a key
for fruit in set5:
    print(fruit)

print("banana" in set5)
print("banana" not in set5)

set5.add("watermelon") #to add new item use add method
print(set5)

tropical = {"pineapple","cherry","papaya"}
set5.update(tropical)
print(set5)

#the object in update() method does not have to be set,it can be any iterable item
list = [1,2,3,4]
set5.update(list)
print(set5)

set5.remove("banana") #use remove method to remove an item,if no item raise error
print(set5)

set5.discard("apple")
print(set5) #we can also use discard,if no item raise no error

#we can use pop but remove random items and return value is removed item


print(set4)
set4.clear() #clear the set
print(set4)
del set4 #delete the set from existence
#print(set4)

for x in set5:
    print(x)

#JOin the sets
# There are several ways to join two or more sets in Python.

# The union() and update() methods joins all items from both sets.

# The intersection() method keeps ONLY the duplicates.

# The difference() method keeps the items from the first set that are not in the other set(s).

# The symmetric_difference() method keeps all items EXCEPT the duplicates.

#union
#returns a new set with all items from both sets
#we can use | instead of union() method

set6 = {"a","b","c","c"}
set7 = {1,2,3}


set8 = set6.union(set7,set3,set5)
#set8 = set6 | set7
print(set8)

x =  {"a","b","c"}
y= (1,2,3)
z = x.union(y)
print(z)

#update()
#inserts  all items from one set to another
#changes the original set and does not return a new set
#both union and update exclude any duplicate items


#intersection
#returns a new set,that only contains the items that are present in both sets
a = {"apple","banana","cherry"}
b= {"google","microsoft","apple"}
c = a.intersection(b)
c = a & b
print(c) #returns only duplicate items(we can also use & operator)

#intesection_update
a.intersection_update(b)
print(a)


set1 = {"apple", 1,  "banana", 0, "cherry"}
set2 = {False, "google", 1, "apple", 2, True}
set3 = set1.intersection(set2)
print(set3)


#Difference
#returns a new set that will contain only the items from first set that are not present in other set
#we can also use - instead of difference()
a = {"apple","banana","cherry"}
b= {"google","microsoft","apple"}
c = a.difference(b)

print(c)

a.difference_update(b)
print(a)


#Symmetric Differences
#keep only the elements that are not present in both the sets
# we can use ^ instead of symmetric_difference()

a = {"apple","banana","cherry"}
b= {"google","microsoft","apple"}
c = a.symmetric_difference(b)
print(c)

a.symmetric_difference_update(b)
print(a)


#frosen set
#unlike sets elements cannot be added or removed from a frozenset
x = frozenset(b)
print(x)
print(type(x))