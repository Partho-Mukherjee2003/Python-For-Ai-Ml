# This is a simple calculator program that takes two numbers and an operator as input and performs the corresponding operation.

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
variable =input('What kind of operation you want to do (\'+\',\'-\',\'*\',\'/\'): ')

if variable == '+':
  print(f"Result:{num1 + num2}")
elif variable == '-':
  print(f"Result:{num1 - num2}")
elif variable == '*':
  print(f"Result:{num1 * num2}")
elif (variable == '/') :
  if num2!=0 :
    print(f"Result:{num1 / num2}")
  else:
    print("Please enter non zero num for division")
elif variable == '%':
  print(f"Result:{num1 % num2}")
else: print("Please enter correct numbers and operators")

