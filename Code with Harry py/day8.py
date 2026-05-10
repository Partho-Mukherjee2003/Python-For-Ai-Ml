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
# print(s1.name,s1.roll,s1.college_name)
# s1.welcome()
# print(s1.returnRoll())
# s2 = Student("Meghla",100)
# print(s2.name,s2.roll,Student.college_name)
# s2.welcome()
# print(s2.returnRoll())

# # class ba object er moddher data gulo ke attribute bole



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
