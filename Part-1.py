#1. Datatypes

name = "bob" #string
num = 45 #integer
cgpa = 9.6 #float
present = True #Boolean

print(type(name))

#string Basics
test= "Apple's products are beautiful"
print(test)

#len() function(count black spaces as well)

text = "Hello world"
print(len(text))
print(text[1])
print(text[0])
print(text[1:4])
print(text[:4])
print(text[2:])

#String Functions
text = "  Hello wORLD     "
print(text.upper())
print(text.lower())
print(text.title())
print(text.count('l'))
print(text.count('rl'))
print(text.find('l'))
print(text.find('z'))
print(text.replace('e','y'))
print(text.replace("wORLD",'planet'))
print(text)
print(len(text))
print(len(text.strip())) #removes the spaces before and after the first and last character
print(text.count(' '))
print(text.strip().count(' '))
address = '102,Bakerst,London'
print(address.split(',')) #split seperate the content of the string accord to specific passed character
# string is broken into list of strings whenerver ',' is observed

test = 'how are you doing'
print(test.split(' '))

output = test.split(' ')
print(output)
print(type(output))

first = "Bill"
last = "Musk"
name = first + last
print(name)

#other way
name = '{}{}'.format(first,last)
print(name)

name = '{} {}'.format(first,last)
print(name)

name = f"{first.upper()} {last.lower()}"
print(name)

#2. Arithmatic Operations

print(10 + 2) #addition
print(10 -2) #substraction
print(10 * 2) #multiplication
print(10 /2) #standard devision
print(10//2) #floor division
print(10 % 2) #modulas

#3. Input and Type Casting

age = input("Enter age:") #input always string so we have to type cast to perform operations
int_age = int(age)
print(int_age + 6)

num1 = int(input("Enter an integer: ")) #we can type cast in this way also
print(num1 + 5)

#4.string Formatting
name1 = "rahul"
score = 95

print(f"student {name1} got {score} in mathematics")

#help(str)
#dir(str)
help(str.upper())