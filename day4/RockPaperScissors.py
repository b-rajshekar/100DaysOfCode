import random

rock = '''
        ___
    ___/   \___
 __/           \__
/                 \
\                 /
 \_______________/       

'''

paper = '''
 __________________
|                  |
|                  |
|                  |
|                  |
|__________________|

'''

scissors = '''
   ____
  / __ \
 ( (__) |___ ___
  \________,'   """""----....____
   _______<  () dd       ____----'
  / __   __`.___-----""""
 ( (__) |
  \____/
  
'''

game_images = [rock, paper, scissors]

# Takes input from the user and store it in user_choice
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for scissors.\n"))

# Prints user choice
print(game_images[user_choice])

# It uses the random
computer = random.randint(0,2)

# Prints computer choice
print("computer chose: ")
print(game_images[computer])

if user_choice == 0 and computer == 2:
    print("You Win!")
elif computer == 0 and user_choice == 2:
    print("You lose")
elif computer > user_choice:
    print("You lose")
elif computer > user_choice:
    print("You win!")
elif computer == user_choice:
    print("Its's a draw")    
else:
    print("You dont know how to play, you lose!")