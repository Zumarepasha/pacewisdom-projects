from random import choice
from words import words
import string

def get_valid_word(words):
    word = choice(words)
    while '-' in word or ' ' in word:
        word =choice(word)
    
    return word.upper()

def hangman():
    word = get_valid_word(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()
    lives = 10

    #getting input
    while len(word_letters) > 0 and lives > 0:
        print("you have ",lives,"left, You have used these letters: "," ".join(used_letters))
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print("Current Word: "," ".join(word_list))

        user_letter = input("Guess a Letter: ").upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives = lives -1
                print("Letter is not in the word")
        elif user_letter in used_letters:
            print("You have guessed that letter already, please try again.")

        else:
            print("invalid character!, please try again")
    
    if lives == 0:
        print("you Died, sorry, The word was ",word)
    else:
        print("you guessed right, the word is ", word, "!!")
        
hangman()