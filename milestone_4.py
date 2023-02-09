import random
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
            print(f"Good guess! {guess} is in the word.")
            for i in range(len(word_chars)):
                if(guess==word_chars[i]):
                    self.word_guessed[i]=guess
                    
            self.num_letters -= 1
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
                print("Invalid letter. Please, enter a single alphabetical character.")
                break
            elif(guess in self.list_of_guesses):
                print("You already tried that letter!")
                break
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)
                break
