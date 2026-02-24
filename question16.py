import random

while True:
    number = random.randint(1, 100)
    attempts = 7

    while attempts > 0:
        guess = int(input("Guess number (1-100): "))
        attempts -= 1

        if guess == number:
            print(" Correct! You guessed it!")
            break
        elif guess > number:
            print("Too High! Attempts left:", attempts)
        else:
            print("Too Low! Attempts left:", attempts)

    if attempts == 0:
        print("You lost! Number was:", number)

    again = input("Play again? (y/n): ")
    if again.lower() != 'y':
        break