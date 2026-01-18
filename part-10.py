#while the condition specified in while statment is true,run through the loop

x= 1
while(x < 5):
    print(x)
    x += 1


x = 1
while(x < 10):
    if x == 4:
        break
    print(x)
    x += 1

while True:
    name = input("Enter a name: ")
    if name == "stop":
        break
    print(name)


i = 0
str = "Beautiful"

while i < len(str):
    if str[i] == "t":
        break
    
    print(f"The current letter: {str[i]} ")
    i += 1