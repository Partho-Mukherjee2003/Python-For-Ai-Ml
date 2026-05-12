import random
computer_Choice = random.choice([-1,0,1])
my_Choice_Number = input("Enter your Choice: ")
word_Dict = {
              "s":-1,
              "w": 1,
              "g": 0
            }
reversed_Word_Dict = {-1:"Snake",1:"Water",0:"Gun"}
my_Choice = word_Dict[my_Choice_Number]

print(f" Your choice:{reversed_Word_Dict[my_Choice]}\n Computer's Choice:{reversed_Word_Dict[computer_Choice]}")

if(my_Choice == computer_Choice):
  print("It's draw.. try again!")
else:
  if(computer_Choice - my_Choice == -2 or computer_Choice - my_Choice == 1):
    print("You are win")
  else:
    print("You are lose")
print("hfoiehfihihifjihfihfihihfihfhfhfifff")
