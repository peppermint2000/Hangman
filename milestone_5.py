import random
fave_fruits= ["apple","banana", "orange", "strawberry", "pear"]
word_list= fave_fruits

class Hangman:
    def __init__(self,word_list,num_lives=5):
        self.word_list= word_list
        self.num_lives=num_lives 
        self.word= random.choice(word_list)
        self.word_guessed= ["_"] * len(self.word)
        self.num_letters=len(set(self.word))
        self.list_of_guesses=[]      
    def ask_for_input(self):
              while True: 
                guess= input("guess the letter?").lower()
                if not guess.isalpha():
                   print("invalid letter , please enter a single alphabetical charecter")
                elif guess in self.list_of_guesses:
                   print("you already tried that letter.")
                else:
                    self.check_guess(guess)
                    self.list_of_guesses.append(guess)
                    return guess
    def check_guess(self,guess):
        if guess in self.word:
                print(f"good guess! {guess} is in the word")
                for i in range(len(self.word)):
                     letter= self.word[i]
                     if letter == guess:
                          self.word_guessed[i]=guess
                self.num_letters -= 1
        else:
                self.num_lives -= 1
                print(f"sorry,{guess} is not in the word")
                print(f"you have {self.num_lives} lives left.")

def play_game(word_list):
    num_lives=5
    game=Hangman(word_list, num_lives=5)
    while True: 
         if game.num_lives== 0:
            print("You lost!")
            break
         elif game.num_letters > 0:
            game.ask_for_input()
         else:
            print("congratulations, you won the game") 
            break

play_game(word_list)





     

     