import random

if __name__ == "__main__":
    word_list = ['mango','blueberries','banana','pineapple','watermelon']
    word = random.choice(word_list)


    def check_guess(guess):
        guess = guess.lower()
        if(guess.isalpha() and len(guess)==1):
            if(guess in word):
                print("Good guess! "+guess+" is in the word")
                return
            else:
                print("Uh oh! That is not in the word")
        else:
            print("Oops! That's not a valid guess. Please enter a single alphabetical character. You're playing hangman!")

    def ask_for_input():
        while(True):
            guess = input("Please pick a letter")
            if(guess.isalpha() and len(guess)==1):
                break
            else:
                print("Oops! That's not a valid guess. Please enter a single alphabetical character. You're playing hangman!")
        check_guess(guess=guess)

