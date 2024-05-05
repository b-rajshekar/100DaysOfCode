coding_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
    "Loop": "The action of doing something over and over again.",
}

#Retrieving items from dictionary.
print(coding_dictionary["Bug"])

#Adding new items to dictionary.
coding_dictionary["spanishWords"] = "Hola, Como estas, Mucho Gusto, Adios."


#Create an empty dictionary.
empty_dictionary = {}

#Wipe an existing dictionary
# coding_dictionary = {}
# print(coding_dictionary)

#Edit an item in a dictionary
coding_dictionary["Bug"] = "A moth in your computer."
print(coding_dictionary)

#Loop through a dictionary
for key in coding_dictionary:
    print(key)
    print(coding_dictionary[key])