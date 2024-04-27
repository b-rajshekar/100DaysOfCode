# names = names_string.split(", ")
names_string = input("Enter a comma-separated list of names: ")  # Get names from user inputv

import random

# Get the total number of items in list.
num_items = len(names_string)
# Generate random numbers between 0 and the last index.
random_choice = random.randint(0, num_items - 1)
# Pick out random person from list of names using the random number.
person_who_will_pay = names_string[random_choice]

print(person_who_will_pay + " is going to buy the meal today!")

#need to do it later