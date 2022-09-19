from random import randint




number = randint(0,10)
stilltrying = True 

print("Welcome to Number guesser, guess the number I have generated")

while stilltrying:

    guessString = input("Guess a number between 0 and 10:")
    answer = int(guessString)
    if answer>10:
        print("What part of between 0 and 10 do you not understand, not funny+didn't laugh")
        exit(1)
    elif answer<0:
        print("Why you type your braincell count")
    else:
        print("Good choice I guess")



    if answer == number: 
        print("Well done, you guessed my number")
        stilltrying = False 
    elif answer>number:
        print("That number is too high, try again")
    else:
        print("That number is too low, try again") 