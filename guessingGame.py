import random

y = random.randint(1,101)
lives = 7
while lives>0:
    x = int(input("Guess the number:"))
    if x!=y and x<y:
           lives-=1
           print("too low, try again lives remaining:",lives)
    if x!=y and x>y:
           lives-=1
           print("too high, try again lives remaining:",lives)
    if lives ==0:
     print("You wasted your lifes, GAME OVER")
    if x==y:
          print("congratulation your answer is correct") 
    
   