# # object oriented programming

# class Car :
#   color = "Blue"
#   brand = "Tata"

# car1 = Car()
# print(car1.brand,car1.color)

# class Student:
#   name = "Partho"
#   roll = 82
# s1 = Student()
# print(s1.name,s1.roll)
# s2 = Student()
# print(s2.name,s2.roll)

# # Constructor / __init__ function # protibar new object create korle constractor call hoy
# class Student:
#   college_name = "BM College" #class attribute - sob object  e same value asbe.
#   name = "anonymous"
#   #Default Constructor # amara call na korleo python bydefault call kore
#   def __init__(self):
#     pass
#   @staticmethod #decorator
#   def hello(): # Static Mathod - don't use self patameter work class level
#     print("hello i am function using staticmethod")
#   #Parameterized Constructor
#   def __init__(self,name,roll):## self perameter == object
#     # self er jaygay jekono kisu likhte pari kintu self lekha professional
#     self.name = name #Object attribute - sob object e alada hbe    {object attribute > class attribute}
#     self.roll = roll

#   def welcome(self): ## Method
#     print("Hello Student,Welcome",self.name)

#   def returnRoll(self): ## Method
#     return self.roll

# s1 = Student("Partho",82)
# s1.hello()
# print(s1.name,s1.roll,s1.college_name)
# s1.welcome()
# print(s1.returnRoll())
# s2 = Student("Meghla",100)
# s2.hello()
# print(s2.name,s2.roll,Student.college_name)
# s2.welcome()
# print(s2.returnRoll())

# # class ba object er moddher data gulo ke attribute bole



# ## Practice Problem
# # 01
# class Student:
#   def __init__(self,name,sub1mark,sub2mark,sub3mark):
#     self.name = name
#     self.sub1mark = sub1mark
#     self.sub2mark = sub2mark
#     self.sub3mark = sub3mark
#   def avarege(self):
#     avarege = ((self.sub1mark + self.sub2mark + self.sub3mark)/3)
#     return round(avarege,3)
# s1 = Student("Partho",95,99,98)
# print(s1.avarege())


# ####
# # Important
# # Abstraction
# # Encapsulation


# # #
# # OOP er 4 ta piller
# # Abstraction - hide the immplemantation details and only show the essential feature
# # Encapsulation - Wrapping data and function into a single unit(Object)
# # Inheritance
# # Polymorphism
# # #

# # Practice Problem
# # 02
# class Account:
#   def __init__(self,balance,acc_no):
#     self.balance = balance
#     self.acc_no = acc_no
#   # Credit Method
#   def credit (self,balance):
#     self.balance += balance
#     print(f"Successfully credited {balance}TK,\n Now your current balance is {self.balance}")
#   # Debit Method
#   def debit (self,balance):
#     if (self.balance >= balance):
#       self.balance -= balance
#       print(f"Successfully debited {balance}TK,\n Now your current balance is {self.balance}")
#     else: print("You do not have sufficient balance")
#   def get_balance(self):
#     return self.balance
# acc1 = Account( 1000 ,1000011112222333)
# acc1.credit(500)
# acc1.debit(1500)

# #Part 2
# class Student:
#   def __init__(self,name,age):
#     self.name = name
#     self.age = age

# s1 = Student('Partho',23)
# print(s1.name,s1.age)
# del s1.name # to delete attribute or object
# print(s1.name)

# # "We can make attributes or methods private by adding __ to the beginning of the attribute or method name."
# class Account:
#   __name = "Anonymous"
#   def __init__(self,acc_no,acc_pass):
#     self.acc_no = acc_no
#     self.__acc_pass = acc_pass
#   def get_password(self):
#     print(self.__acc_pass)
#   def __hello(self):
#     print("Hello Person",self.__name)
#   def welcome(self):
#     self.__hello()
# acc1 = Account(1234,5060)
# #print(acc1.acc_no,acc1.__acc_pass) ## __acc_pass is the prive attribute.thats why we cannot access out of the account class scope
# acc1.get_password()
# #print(acc1.__name,acc1.__hello()) ##return error because these are private
# acc1.welcome()



# # Inheritance--   1.Single inheritance    2.Multi level inheritance    3.Multi inheritance
# class Car:
#   def __init__(self,typ,color):
#     self.typ = typ
#     self.color = color

#   @staticmethod
#   def start():
#     print("The car is starting")

#   @staticmethod
#   def stop():
#     print("The car is stoping")
# class Marcides(Car):   # aivabe amra multi level inheritance use korte pari..
#     def __init__(self,brand,typ,color):
#         self.brand = brand
#         super().__init__(typ,color) ## this is super method use to access method of the parent class
#         super().start()


# car1 = Marcides('Marcides','Electric','blue')
# print(car1.brand,car1.typ,car1.color)



# class A:
#   a = "This is the class A"
# class B:
#   b = "This is the class B"

# class C(A,B): # Multi inheritance
#   c="This the class C"

# c = C()
# print(c.c,c.a,c.b)


# #  Class  method
# class Person:
#   name = "Partho"
#   age = 23

#   def changeName(self,name):
#     self.__class__.name = name  ## self.Person.name

#   @classmethod ## This is the class method is using change the value of class attribute
#   def changeAge(cls,age):
#     cls.age = age


# p1 = Person(  )
# p1.changeName('Mr. mukherjee')
# p1.changeAge(21)
# print(p1.name)
# print(Person.name)
# print(p1.age)
# print(Person.age)

# # Methods
# # 1.Statistic Methods
# # 2.Class Methods (cls)
# # 3.Instance Methods (self)
# # #

# #  Property decorator -- we use on any method in the class to use the method as a property
# # propertyr value sohoje change kore
# class Student:
#   def __init__(self,phy,che,math):
#     self.phy = phy
#     self.che = che
#     self.math = math

#   @property
#   def avarage(self):
#     return round(((self.phy + self.che + self.math) / 3), 3)


# stu = Student(99, 98 , 99)
# print(stu.avarage)
# stu = Student(85, 98 , 87)
# print(stu.avarage)


# @property.getter
# @property.setter

# # Polymorphism : Oparetor Over loading
# # same oparetor is allow to have different meaning According to the context#

# class Complex():
#   def __init__(self,real,img):
#     self.real = real
#     self.img = img

#   def showNumber(self):
#     print(f"{self.real}i + {self.img}j")

#   def __add__(self, num2): # Dunder Function
#     realNumber = self.real + num2.real
#     imgNumber = self.img + num2.img
#     return Complex(realNumber,imgNumber)
#   def __sub__(self, num2):
#     realNumber = self.real - num2.real
#     imgNumber = self.img - num2.img
#     return Complex(realNumber,imgNumber)


# complex1 = Complex(2,4)
# complex1.showNumber()
# complex2 = Complex(1,3)
# complex2.showNumber()
# complex3 = complex1 + complex2
# complex3.showNumber()
# complex4 = complex1 - complex2
# complex4.showNumber()


# # Practice Problem
# # 01#
# import math
# class Circle:
#   def __init__(self,r):
#     self.r = r

#   def area(self):
#     return round(math.pi * self.r**2,3)

#   def perimeter(self):
#     return round(2 * math.pi * (self.r),3)


# cir1 = Circle(5)
# area1 = cir1.area()
# perimeter1 = cir1.perimeter()
# print(area1,perimeter1)

# # 02 #
# class Employee:
#   def __init__(self,role,department,salary):
#     self.role = role
#     self.department = department
#     self.salary = salary

#   def showDetails(self):
#     print(f"Employee's role is {self.role}")
#     print(f"Employee's department is {self.department}")
#     print(f"Employee's salary is {self.salary}")


# class Engineer(Employee):
#   def __init__(self,name,age,role,department,salary):
#     self.name = name
#     self.age = age
#     super().__init__(role,department,salary)


# person1 = Engineer('Partho',21,"js developer","developer",15000)
# print(person1.name ,person1.role)
