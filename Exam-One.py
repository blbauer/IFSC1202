# This is a guess the number game.
# Import the Random Integer Function
from random import randint
# Prompt for the Name
myName = input('Hello! What is your name? ')
# Display Greeting
print("Well, " + myName + ", I am thinking of a number between 1 and 20.")
print("You have 5 guesses.")
# Pick a random number between 1 and 20
number = randint(1, 20)
# Make five guesses
for guessesTaken in range(1,6):
    guess = int(input("Take a guess: "))
    # Check for guess less than number
    if guess < number:
        print("Your guess is too low.")
    # Check for guess greater than number
    if guess > number:
        print("Your guess is too high.")
    # Check for the correct guess
    if guess == number:
        print("Good job, " + myName + "! You guessed my number in " + str(guessesTaken) + " guesses!")
    # Exit the loop for a correct guess
        break
    # Either we have had more than 5 guesses or the correct guess was enter
    # if the guess was not correct, then display the appropriate message
if guess != number:
    print("Nope. The number I was thinking of was " + str(number))