""" Build a program that takes User Bill Amount in dollars, how many people would like to split the bill and what is
the tip percentage (10, 12, 15). The Final Output should include how much each person should pay (including tip)
Learning: Python Primitive Data types, Type Conversion and Type Checking, Mathematical Operations in Python
"""

print("Welcome to the Tip Calculator")
Total_bill = float(input("What is the Bill Amount?\n$"))
Percentage_tip = int(input("What percentage tip would you like to give, 10, 12,or 15?\n"))
People_split = int(input("How many people would like to spilt the bill?\n"))

Tip_Bill = (Total_bill + (Total_bill * (Percentage_tip / 100)))
Final_Bill = Tip_Bill / People_split
Final_Bill = "{:.2f}".format(Final_Bill) # To get upto 2 decimal places as usual bill shows.
print(f"Each Person Should Pay: ${Final_Bill}")

#print(type(Final_Bill))