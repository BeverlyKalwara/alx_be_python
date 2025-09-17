import random

print("🎲 Welcome to the Number Guessing Game!")

while True:
    # Generate secret number
    secret_number = random.randint(1, 10)
    counter = 0 #No of Tries

    while True:  # keep guessing until correct
        try:
            guess = int(input("I'm thinking of a number between 1 and 10. Can you guess it? "))
            counter += 1  # increment counter on each guess

            match guess:
                case _ if guess == secret_number:
                    print("🎉 Congratulations, you guessed it!")
                    break
                case _ if guess < secret_number:
                    print("Nope, your guess is a bit low. Give it another shot!")
                case _ if guess > secret_number:
                    print("Oops, your guess is a bit high. Try again!")
                case _:
                    print("Invalid input!")
        except ValueError:
            print("⚠️ Please enter a valid number!")

    # Ask if the player wants to play again
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        print("Thanks for playing! 👋")
        break