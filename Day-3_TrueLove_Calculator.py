"""In this calculator, Take both people's names and check for the number of times the letters in the word TRUE occurs.

Then check for the number of times the letters in the word LOVE occurs.

Then combine these numbers to make a 2 digit number.

For Love Scores less than 10 or greater than 90, the message should be:

"Your score is *x*, you go together like coke and mentos."
For Love Scores between 40 and 50, the message should be:

"Your score is *y*, you are alright together."
Otherwise, the message will just be their score. e.g.:

"Your score is *z*."
e.g.

name1 = "Angela Yu"
name2 = "Jack Bauer"
T occurs 0 times

R occurs 1 time

U occurs 2 times

E occurs 2 times

Total = 5

L occurs 1 time

O occurs 0 times

V occurs 0 times

E occurs 2 times

Total = 3

Love Score = 53

Print: "Your score is 53.""""

# This execise was part of 100 Days course and we had to implement our own solution which is below.

print("The Love Calculator is calculating your score...")
name1 = input() # What is your name?
name2 = input() # What is their name?

name11 = name1.upper()
name22 = name2.upper()
calT = name11.count('T') + name11.count('R') + name11.count('U') + name11.count('E') + name22.count('T')  + name22.count('R') + name22.count('U') + name22.count('E')
calL = name11.count('L') + name11.count('O') + name11.count('V') + name11.count('E') + name22.count('L')  + name22.count('O') + name22.count('V') + name22.count('E')

a = f"{calT}{calL}"
c = int(a)

if 40<= c <= 50:
  print(f"Your score is {calT}{calL}, you are alright together.")

elif c >= 90 or c <= 10:
  print(f"Your score is {calT}{calL}, you go together like coke and mentos.")
else:
  print(f"Your score is {calT}{calL}.")
