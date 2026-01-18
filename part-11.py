#classes and objects

class Employee:
    name = "john"
    age = 34

    def hello(self):
        print("Hello")

emp = Employee()
print(type(emp))

#object is an instance of class
#class represent an entity(in this case employee)

#object of a class can access attributes of the class
print(emp.name)
print(emp.age)
emp.hello()

#Attributes and Methods

class Employee:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def details(self):
        print("Employee name: ",self.name)
        print("Employees age: ",self.age)

emp1 = Employee("john",45)
emp2 = Employee("anurag",34)

emp1.details()
emp2.details()


class Student:
    def __init__(self,name):
        self.name = name

    def introduction(self):
            print("Hi my name is",self.name)
        
    def change_name(self,name):
            self.name = name

s1 = Student("Anurag")
s1.introduction()
s1.change_name("bob")
s1.introduction()


class Rectangle:
     def __init__(self,length,width):
          self.length = length
          self.width = width

     def area(self):
          area = self.length * self.width
          return area
     
first = Rectangle(12,23)
print(first.area())


class Dog:
     def __init__(self,name,breed,age,color):
          self.name = name
          self.breed = breed
          self.age = age
          self.color = color
    
     def details(self):
          print(f"{self.name} has breed{self.breed} and age{self.age} and color is{self.color}")
     
     def woof(self):
          print("WOOF!")

Dog1 = Dog("Rocky","German Shephard",12,"black")
Dog1.details()
Dog1.woof()
print(Dog1.age)
          