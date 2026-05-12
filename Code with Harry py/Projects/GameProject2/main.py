import  random
n = random.randint(1,100)
a= 0
guess = 0
while(a != n):
  a = int(input("Guess the correct number (1 to 100):"))
  if( a == 0 or 100 <= a ):
    print("Please guess the  number between (1 to 100)")
  else:
    if(a < n):
      print("Higher number please!")
    elif(a > n):
      print("Lower number please!")
  guess = guess + 1

print(f"You guess the right number {a} at {guess} attempt !")
