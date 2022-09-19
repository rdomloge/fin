from random import randint

number = randint(0,10)
stilltrying = True 
count = 0
print("Welcome to Number guesser, guess the number I have generated")

while stilltrying:

    guessString = input("Guess a number between 0 and 10:")
    answer = int(guessString)
    count = count+1

    print("Attempt ",count,"") 
    if answer == number: 
        print("Well done, you guessed my number")
        print("Well done, you did this in ",count," tries")
        stilltrying = False 
    elif answer>number:
        print("That number is too high, try again")
    else:
        print("That number is too low, try again") 