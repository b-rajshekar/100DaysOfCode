import random
word_list = ["ardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

print(f"Pssst, the solution is {chosen_word}.")


#Ask the user to guess a letter and assign their answer to a variable called guress. Make guess lowercase.
guess = input("Guess a letter: ").lower()

#Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
for letter in chosen_word:
    if letter == guess:
        print("Right")
    else:
        print("Wrong")