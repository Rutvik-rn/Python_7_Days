import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

word_list = ["apple","banana", "cherry", "tiger", "elephant", "dolphin", "giraffe", "penguin", "koala", "cheetah", 
             "kangaroo", "panda", "eagle","orange", "mango", "strawberry", "pineapple", "watermelon", "grape", "kiwi"]

chosen_word = ""

for i in range(1):
    chosen_word+= random.choice(word_list)

print(chosen_word)

# Creating a list full of blanks
blank = []

for number_of_blanks in chosen_word:
    blank.append("_")

# Creating a variable lives = total lives available in game
lives = 6
# While Loop to allow User to guess and keep playing the game
game_over = False
while not game_over:
    guess = input("Guess a Character For your Word ").lower()

    for j in range(len(chosen_word)):
        letter = chosen_word[j]
        if letter == guess:
            blank[j] = letter
            print(lives)

    if guess not in chosen_word:
        lives -= 1
        print(f"Lives Remaining: {lives}")
        if lives == 0:
            game_over =True
            print("You Lost")
            print(f"Your Word was {chosen_word}") 

            

    print(blank)
    print(f"{''.join(blank)}")

    if "_" not in blank:
        game_over = True
        print("you win")
    
    print(stages[lives])




        



