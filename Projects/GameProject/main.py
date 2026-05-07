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
print(my_Choice)
