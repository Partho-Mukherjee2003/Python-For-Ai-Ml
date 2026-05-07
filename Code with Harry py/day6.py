# def sum():
#   a = int(input("Enter a number: "))
#   b = int(input("Enter a number: "))
#   print(a + b)

# sum()

# def hello(name,ending="this is by default perameter"):
#   print(f"good morning {name}")
#   print(ending)

# hello("Partho","Thanks")
# hello("Meghla","Thank you")


# recursion function
# def factorial(n):
#   if( n==0 or n==1 ):
#     return 1
#   return n * factorial(n-1)

# n = int(input("Enter a number:"))
# print(f"The factorial is: {factorial(n)}")

# problem 01
# print("A")
# print("B")
# print("C" , end="")
# print("D" , end="")

# # Problem 02
# def sum_number_recursive(n):
#   if(n==1):
#     return 1
#   return n + sum_number_recursive(n-1)

# n = int(input("Enter a number: "))

# print(f"The sum of {n} is:{sum_number_recursive(n)}")

# Problem 03
# def pattern (n):
#   if(n==0):
#     return
#   print("*" * n)
#   pattern(n-1)

# n = int(input("Enter a number: "))
# print(pattern(n))

# problem 04

# def strip(l , word):
#   n=[]
#   for i in l:
#     if not(i == word):
#       n.append(i.strip(word))
#   return n

# l =['Partho','Proma','Piyal','Proshonjit','Prity','P']
# print(strip(l , 'P'))

