# object oriented programming

class Car :
  color = "Blue"
  brand = "Tata"

car1 = Car()
print(car1.brand,car1.color)

class Student:
  name = "Partho"
  roll = 82
s1 = Student()
print(s1.name,s1.roll)
s2 = Student()
print(s2.name,s2.roll)

# Constructor / __init__ function # protibar new object create korle constractor call hoy
class Student:
  college_name = "BM College" #class attribute - sob object  e same value asbe.
  name = "anonymous"
  #Default Constructor # amara call na korleo python bydefault call kore
  def __init__(self):
    pass
  @staticmethod #decorator
  def hello(): # Static Mathod - don't use self patameter work class level
    print("hello i am function using staticmethod")
  #Parameterized Constructor
  def __init__(self,name,roll):## self perameter == object
    # self er jaygay jekono kisu likhte pari kintu self lekha professional
    self.name = name #Object attribute - sob object e alada hbe    {object attribute > class attribute}
    self.roll = roll

  def welcome(self): ## Method
    print("Hello Student,Welcome",self.name)

  def returnRoll(self): ## Method
    return self.roll

s1 = Student("Partho",82)
s1.hello()
print(s1.name,s1.roll,s1.college_name)
s1.welcome()
print(s1.returnRoll())
s2 = Student("Meghla",100)
s2.hello()
print(s2.name,s2.roll,Student.college_name)
s2.welcome()
print(s2.returnRoll())

# class ba object er moddher data gulo ke attribute bole



## Practice Problem
# 01
class Student:
  def __init__(self,name,sub1mark,sub2mark,sub3mark):
    self.name = name
    self.sub1mark = sub1mark
    self.sub2mark = sub2mark
    self.sub3mark = sub3mark
  def avarege(self):
    avarege = ((self.sub1mark + self.sub2mark + self.sub3mark)/3)
    return round(avarege,3)
s1 = Student("Partho",95,99,98)
print(s1.avarege())


####
# Important
# Abstraction
# Encapsulation


# #
# OOP er 4 ta piller
# Abstraction - hide the immplemantation details and only show the essential feature
# Encapsulation - Wrapping data and function into a single unit(Object)
# Inheritance
# Polymorphism
# #

# Practice Problem
# 02
class Account:
  def __init__(self,balance,acc_no):
    self.balance = balance
    self.acc_no = acc_no
  # Credit Method
  def credit (self,balance):
    self.balance += balance
    print(f"Successfully credited {balance}TK,\n Now your current balance is {self.balance}")
  # Debit Method
  def debit (self,balance):
    if (self.balance >= balance):
      self.balance -= balance
      print(f"Successfully debited {balance}TK,\n Now your current balance is {self.balance}")
    else: print("You do not have sufficient balance")
  def get_balance(self):
    return self.balance
acc1 = Account( 1000 ,1000011112222333)
acc1.credit(500)
acc1.debit(1500)
