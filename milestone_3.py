import random

word_list = ['mango','blueberries','banana','pineapple','watermelon']
word = random.choice(word_list)


def check_guess(guess):
    guess = guess.lower()
    if guess in word:
        print(f"Good guess! {guess} is in the word")
        return
    else:
        print("Uh oh! That is not in the word")

def ask_for_input():
    while True:
        guess = input("Please pick a letter")
        check_guess(guess=guess)

        if guess.isalpha() and len(guess)==1:
            break
        else:
            print("Oops! That's not a valid guess. Please enter a single alphabetical character. You're playing hangman!")
    return ask_for_input()
ask_for_input()


