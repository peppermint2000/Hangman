import random

fave_fruits= ["apple","banana", "orange", "strawberry", "pear"]
word_list= fave_fruits
print(word_list)

word=  random.choice(word_list)

guess_work= input(("put a single letter"))
print("You entered:", guess_work)
if len(guess_work)== 1 and guess_work.isalpha(): 
    print("good guess")
else: 
    print("oops not valid input")
