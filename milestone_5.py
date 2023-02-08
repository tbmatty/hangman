#%%

import random


def play_game(word_list):
    num_lives = 5
    word_list = ['mango','blueberries','banana','pineapple','watermelon']

    game = Hangman(num_lives=num_lives, word_list=word_list)
    while(True):
        if(game.num_lives<=0):
            print("You lose!")
            break
        if(game.num_letters>0):
            game.ask_for_input()
        if(game.num_lives != 0 and game.num_letters<=0):
            print("You won")
            break


class Hangman:

    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(word_list)
        self.word_guessed = ['_' for i in range(len(self.word))]
        self.num_letters = len(list(set(self.word)))
        self.list_of_guesses = []
    
    def check_guess(self,guess):
        guess = guess.lower()
        word_chars = self.word.split()

        if(guess in self.word):
            print("Good guess! "+guess+" is in the word")
            for i in range(len(word_chars)):
                if(guess==word_chars[i]):
                    self.word_guessed[i]=guess
                    self.num_letters = self.num_letters -1 
            print("num letters: "+str(self.num_letters))          
        else:
            self.num_lives -= 1
            print("Uh oh! That is not in the word")
            print("You have "+str(self.num_lives)+" lives left")
        self.list_of_guesses.append(guess)
        return 

    def ask_for_input(self):
        while(True):
            guess = input("Please pick a letter")
            if(not(guess.isalpha() and len(guess)==1)):
                print("Invalid letter. What the heck! Enter a single alphabetical character")
            elif(guess in self.list_of_guesses):
                print("Oops! You silly goose. You've already guessed that letter.")
            else:
                self.check_guess(guess)


play_game(5)


# %%
