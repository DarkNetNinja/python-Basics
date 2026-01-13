#Function is a organized block of reusable code which can be called whenever required

def hello():
    print("Hello world")

# hello()


def hello(name):
    print(f"hello {name}")

hello("Anurag")
hello(int(12))
print(type(hello))

def addthis(first,second):
    print(first + second)

addthis(23,34)

def hello_you(name):
    return (f"hello {name.upper()}")

print(hello_you("Anurag"))


def hi(name):
    message = "hi " + name
    return message


# name = input("Enter a name: ")
# print(hi(name))

def add():
    a = 23
    b = 23
    return a + b

print("this sum is: ",add())


def add(a,b):
    return a + b

a = int(input("Enter a: "))
b= int(input("Enter b: "))
print("Sum = ",add(a,b))

p = int(input("Enter the principle amoundt? "))
t = float(input("Enter the rate of interest? "))
r = int(input("Enter the time in years? "))

# def interest_calc(p,t,r):
#     return (p*t*r)/100

# print("Simple interest: ",interest_calc(p,t,r))

def find_distance(speed,time):
    print(speed,time)
    return speed * time

d = find_distance(speed = 23,time = 2)
print(d)

d = find_distance(time = 12,speed = 34)
print(d)

d = find_distance(3,10)
print(d)

