a = 33
b = 345

if a> b:
    print("a is bigger than b")
else:
    print("a is smaller than b")

# num = int(input("Enter a number: "))

# if(num % 2) == 0:    
#     print("The number is even")
# elif(num%2) != 0:
#     print("odd")
# else:
#     print("The number is zero")

#using if statement we can find the largest number

def input_num():
     s = int(input("Enter an number: "))
     return s

a = input_num()
b = input_num()
c = input_num()

if a> b and a>c:
    print("a is largest")
if b > a and b > c:
    print("b is largest")
if c > a and c > b:
    print("c is largest")

age = int(input("Enter your age: "))

if age >= 18:
    print("you are an adult")
else: 
    print("you are a minor")

#check whether the input number is 30,40 and 50

number = int(input("Enter a number: "))

if number == 30:
    print("Tne number is 30")
elif number == 40:
    print("the number is 40")
elif number == 50:
    print("the number is 50")
else: 
    print("i can count anything else")

#Nested if
x = 34

if x > 10:
    print("above ten")
    if x > 20:
        print("above 20")
    else:
        print("not above 20")

#shortcut

a = 2
b =45
print("a") if a>b else print("b")

