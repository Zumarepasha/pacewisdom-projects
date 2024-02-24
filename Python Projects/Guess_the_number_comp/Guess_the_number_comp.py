from random import randint

def guess(x):
    rand_numb = randint(1,x)
    guessed = 0

    while guessed != rand_numb:
        guessed = int(input("Enter the guess: "))
        if guessed < rand_numb:
            print("Sorry you guessed wrong, its low...")
        elif guessed > rand_numb:
            print("Sorry you guesses wrong, its high...")
    print("yay you guessed right!!....")


guess(100)