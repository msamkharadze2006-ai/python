import random
x= random.randint(1,101)
lives = 7
consecutive_high = 0
consecutive_low =0


while lives >0:
    number_guessed = int(input("Guess a number between 1 and 100: "))
    if number_guessed == x:
        
        print("You guessed the number correctly, you live, for now...")
        break
    elif number_guessed > x:
        print("Your guess is too high.")
        consecutive_high += 1
        consecutive_low = 0
        lives -= 1
    elif number_guessed < x:
        print("Your guess is too low.")
        consecutive_low += 1
        consecutive_high = 0
        lives -= 1
    elif consecutive_high == 3: 
        print("You have guessed too high 3 times in a row, think lower, think mark.")
    elif consecutive_low == 3:
        print("You have guessed too low 3 times in a row. think higher or else....")

if lives == 0:
    print("You have run out of lives, time to face consequences.")
    
