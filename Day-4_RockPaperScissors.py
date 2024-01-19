"""Building a fun Rock, Paper & Scissors Game. User plays against the computer to see if they can win. 
Note: Enter 0 for Rock, 1 for Paper and 2 for Scissors.
Learnings: random(),randint()
"""

import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

user_input = int(input("What Would You Like to Choose: 0 = Rock, 1 = Paper & 2 = Scissors.\n"))

if user_input == 0:
    print("You Choose\n" + rock + "Rock\n")

elif user_input == 1:
    print("You Choose\n" + paper + "Paper\n")

elif user_input == 2:
    print("You Choose\n" + scissors + "Scissors\n")


computer_input = random.randint(0,2)

if computer_input == 0:
    print("The Computer Choose\n" + rock + "Rock")

elif computer_input == 1:
    print("The Computer Choose\n" + paper + "Paper")

elif computer_input == 2:
    print("The Computer Choose\n" + scissors + "Scissors")


if user_input == 0 and computer_input == 0:
    print("Match Tie")

elif user_input == 0 and computer_input == 1:
    print("Computer Wins!!, You Loose, Another go?")

elif user_input == 0 and computer_input == 2:
    print("You Win!!, Another go?")

elif user_input == 1 and computer_input == 0:
    print("You Win!!, Another go?")

elif user_input == 1 and computer_input == 1:
    print("Match Tie, Another go?")

elif user_input == 1 and computer_input == 2:
    print("Computer Wins!!, You Loose, Another go?")

elif user_input == 2 and computer_input == 0:
    print("Computer Wins!!, You Loose, Another go?")

elif user_input == 2 and computer_input == 1:
    print("You Win, Another go?")

elif user_input == 2 and computer_input == 2:
    print("Match Tie, Another go?")




