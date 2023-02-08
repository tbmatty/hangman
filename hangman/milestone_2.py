#%%

import random
word_list = ['mango','blueberries','banana','pineapple','watermelon']
print(word_list)
word = random.choice(word_list)
print(word)
guess = input("Enter your guess")
if(guess.isalpha() and len(guess)==1):
    print("Good guess")
else:
    print("Oops! That is not a valid input.")


# %%
