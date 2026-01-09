#Comparison Operators (result either True or False)

print(2 == 2) #equal to
print(2 == 1)

print(3 != 2) #not equal to
print(3 < 2) #less than
print(2 < 3)
print(3 > 4) #greater than
print(4 > 3)
print(3 <= 3) #less than equal to
print(3 >= 2) #greater than equal to

#Assignment Operator

num = 5
print(num)
num += 4 #shortcut for add and assign
print(num)
num -= 2
print(num)
num *= 2
print(num)
num /= 2
print(num)
num //= 2
print(num)
num **= 2
print(num)

#Logical Operators

#logical and
print(True and False)
print(True & True)
print(False & False)
print(False & True)

#logical or
print(True or False)
print(True | True)
print(False | False)
print(False | True)

#logical not(oposite of something)
print(not False)
print(not True)

x = 5
print(x > 4 and x < 6)

print(x > 3 or x < 4)

print(not(x > 3 and x < 10))

#int float functions

print(abs(-5))
print(abs(-5.67))

print(round(3.45))
print(round(-4.56))

#rounding with precision
print(round(3.454335443,2))
print(round(-4.56435634,4))

#TypeCasting
num1 = int(input("Enter an integer 1: "))
num2 = int(input("Enter an integer 2: "))

print(num1 + num2)

num = 0
num = bool(num)
print(num)

#if-else comparison

x = 5
y = 4
if x > 4:
    print("x is greater than y")
else:
    print("x is smaller than y")

#practice
height = 175
if height > 150:
    print("This building is tall")
elif height < 150:
    print("This Building is small")
else:
    print("There is no Building its an illusion")


#2
is_subscribe = True
if is_subscribe:
    print("Thank you for your subscription")
else:
    print("Please Subscribe")

#3
x = 7
if x > 10:
    print("x is greater than 10")
    if x > 20:
        print("x is grater than 20")
        if x > 30:
            print("x is greater than 30")
        else:
            print("x is smaller than 30")
    else:
        print("x is smaller than 20")
else:
    print("x is smaller than 10")

