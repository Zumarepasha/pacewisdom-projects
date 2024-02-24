from random import randint

def guess(x):
    low = 1
    high = x
    feedback = ""

    while feedback != 'c':
        if low != high:
            guessed = randint(low,high)
        else:
            guessed = low
        feedback = input(f"please say the guessed {guessed} is correct(c), or high(h) or low(l): ")
        if feedback == 'h':
            high = guessed - 1
        elif feedback == 'l':
            low = guessed + 1

    print ("yes I guessed right!...")

guess(100)
