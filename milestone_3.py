import random

fave_fruits= ["apple","banana", "orange", "strawberry", "pear"]
word_list= fave_fruits
print(word_list)
secret_word=random.choice(word_list)
print(secret_word)


while True:
    guess=input("whats the letter?")
    if guess.isalpha():
        if guess in secret_word:
            print(f"welldone, {guess} is in your word is in fave fruit")
        else: 
            print(f"sorry {guess} not in the fave fruit")
            break
    else: 
        print("invalid letter, please ,enter a single alphabitical charaecter")
        break 
    break
if __name__ == "__main__":
    def check_guess(guess, secret_word):
      guess=guess.lower()
      if guess in secret_word:
        print(f"welldone, {guess} is in your word is in fave fruit")
        return True 
      else: 
        print(f"sorry {guess} not in the fave fruit")
        return False



def ask_for_input(secret_word):
        while True:
            guess=input("guess letter?")
            if guess.isalpha():
                result=check_guess(guess, secret_word)
                if result:
                    break 
            else:
                print("invalid input,enter a single alphabetical character")

ask_for_input(secret_word)

 


