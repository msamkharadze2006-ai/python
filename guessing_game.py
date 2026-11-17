import random

def guessing_game():
    # Generate random number between 1-100
    secret_number = random.randint(1, 100)
    lives = 7
    attempts = 0
    consecutive_wrong = 0
    
    print("=" * 50)
    print("WELCOME TO THE GUESSING GAME!")
    print("=" * 50)
    print(f"You have {lives} lives. Use them wisely!\n")
    
    while lives > 0:
        try:
            # Get user input
            guess = int(input("guess the number from 1-100: "))
            
            # Validate input range
            if guess < 1 or guess > 100:
                print("⚠️  Please guess a number between 1 and 100!\n")
                continue
            
            attempts += 1
            consecutive_wrong += 1
            
            # Check if guess is correct
            if guess == secret_number:
                # First try - special message
                if attempts == 1:
                    print("\n🤨 NO WAY YOU CHEATED\n")
                else:
                    print("\n🎉 YEESSS GOOD JOBBB 🎉\n")
                
                # Message based on number of attempts
                if attempts > 5:
                    print("⏳ FINALLY it felt like eternity\n")
                
                print(f"You guessed the number {secret_number} in {attempts} attempts!")
                print("=" * 50)
                break
            
            # Guess is too high
            elif guess > secret_number:
                lives -= 1
                print(f"its too high")
                print(f"Lives remaining: {lives}\n")
                
                # Check for consecutive wrong answers
                if consecutive_wrong >= 3:
                    print("💀 you suck get better\n")
            
            # Guess is too low
            else:
                lives -= 1
                print(f"thats too loowww")
                print(f"Lives remaining: {lives}\n")
                
                # Check for consecutive wrong answers
                if consecutive_wrong >= 3:
                    print("💀 you suck get better\n")
        
        except ValueError:
            print("❌ Invalid input! Please enter a valid number.\n")
            continue
    
    # Game over - lost all lives
    if lives == 0:
        print("\n" + "=" * 50)
        print("💀 GAME OVER 💀")
        print("=" * 50)
        print(f"YOU HAD SEVEN LIVES AND SOMEHOW U FUCKED UP")
        print(f"The number was: {secret_number}")
        print("=" * 50)

# Run the game
if __name__ == "__main__":
    guessing_game()
    
    # Ask if player wants to play again
    while True:
        play_again = input("\nDo you want to play again? (yes/no): ").lower()
        if play_again == "yes" or play_again == "y":
            print("\n" * 2)
            guessing_game()
        elif play_again == "no" or play_again == "n":
            print("Thanks for playing! Goodbye! 👋")
            break
        else:
            print("Please enter 'yes' or 'no'")
