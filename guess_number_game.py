import random

def guess_the_number():
    number_to_guess = random.randint(1, 10)
    attempts = 0

    print("===================================")
    print("|     Welcome to Guess the Number  |")
    print("|----------------------------------|")
    print("|   I've chosen a number between   |")
    print("|            1 and 10.             |")
    print("|        Can you guess it?         |")
    print("===================================")

    while True:
        user_guess = int(input("\nEnter your guess: "))
        attempts += 1

        if user_guess < number_to_guess:
            print("Too low! Try again.")
        elif user_guess > number_to_guess:
            print("Too high! Try again.")
        else:
            print("=====================================================================")
            print("|                          Congratulations!                         |")
            print(f"|              You guessed the number {number_to_guess} in {attempts} attempts!              |")
            print("=====================================================================")
            break

guess_the_number()
