import random

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

guesses = []


keep_playing = True

while keep_playing:
    number = random.randint(1, 100)
    guesses = []  

    print("Try to guess the number!")
    
    guessed = False
    while not guessed:
        guess = input("Enter your guess: ")
        guess = int(guess)
        
        guesses.append(guess)
        
        if guess == number:
            print("Correct! You guessed it!")
            guessed = True
        elif guess < number:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")
    
    print("Your guesses were:", guesses)
    print("It took you", len(guesses), "guesses!")
    
    answer = input("Play again? (yes/no): ")
    if answer == "no":
        keep_playing = False

print("Thanks for playing")

