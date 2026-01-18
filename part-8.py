#for loop
#use for loop to iterate through list
courses = ['ba','bcom','bsc','be']
for course in courses:
    print(course)

#use for loop to iterate through tuple
fruits = ('apple','tesla','banana','mango')
for fruit in fruits:
    print(fruit)

#use for loop to iterate through a dictionary
company = {'name':'tesla',
           'founder':'elon',
           'year':2004}

for  item in company:
    print(item,company[item])

#use for loop to iterate through string
text ='Hello'
for i in text:
    print(i)

#range( ) comes handy using for loop

for i in range(5):
    print(i)

print('------')

for i in range(1,8):
    print(i)

#use enumerate for getting index

courses =['ba','bcom','bsc','be']
for id,item in enumerate(courses):
    print(id,item)


#another way without using enumerate

for i in range(len(courses)):
    print(i,courses[i])

#we can use condition inside for loop
for course in courses:
        if course == 'bcom':
            print(course)
        else:
            print('Couses is NOT bcom')

#Break 
courses = ['ba', 'bcom', 'bsc', 'be']
for item in courses:
    if item == 'bsc':
        break
    print(item)

for course in courses:
    if course == 'bsc':
        continue
    print(course)

for item in range(len(courses)):
    print(item,courses[item])

# name = input('enter your name---')
# print('lets print character seperately')
# for char in name:
#     print(char)


nums = [1,2,3,4,5,6]

def square(item):
    return item * item
    
    
for i in nums:
    print(i,square(i))

#This give the sum of the given list

num = [10,20,30,40]
sum = 0
for i in num:
    sum = sum + i
print("The sum is:",sum)


#This give the multiplication table

# num = int(input("enter an integer: "))
# for i in range(1,11):
#     print(f"{num} x {i} = {num * i}")

#for loop inside loop

adj = ["red","big","tasty"] #outer loop
fruits = ["apple","banana","cherry"] #innerloop

for x in adj:
    for y in fruits:
        print(x,y)


#NESTED loop
# for i in range(4):
#     for j in range(20,24):
#         print(i,j)

# rows = int(input("enter the rows: "))
# for row in range(0,rows - 1):
#     for col in range(row):
#         print("*",end = ' ')
#     print()

# rows = int(input("enter the rows: "))
# for i in range(0,rows+1):
#     for j in range(i):
#         print(i,end =' ')
#     print()

rows = int(input("Enter the no of rows: "))
for i in range(0,rows+1):
    for j in range(i):
        print(i,end =" ")
    print()

list = [12,34,45,67]

count = 0
for item in list:
    count += 1

print(count)


nums = [12,34,56,30]
i = int(input("Enter an number: "))
index = 0
for num in nums:
    if num == i:
        print(f"the index of {i} is {index}")
        break
    else:
        index += 1

letters = ['a', 'b', 'c', 'd', 'e']
index = 0
for letter in letters:
    if letter == 'c':
        print(f"{letter} is found at {index}")
        break
    else:
        index += 1
    