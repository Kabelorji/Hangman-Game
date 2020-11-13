#Import word list

file_name = "python class/datastructures/words.txt"
file = open(file_name, "r")

#open word list and split with commas
data = file.read( ).split(',')
print(data)


# import the funtion random
import random

selected_word = random.choice(data)

# python choices a random word and request for a guess
print("I have selected a word")

guessed_letters_list = [] 
turns = 5

while turns:
    guessed_letter = input("PLEASE, GUESS A LETTER : ")

# if guessed letter is correct, it will be added to an empty list to make up the word
    if guessed_letter in selected_word :
        guessed_letters_list.append(guessed_letter)

# if guess letter is incorrect, you lose a turn
    else:
        turns -= 1
        # print(True)

    for letter in selected_word :


# every letter guesed will be printed on one line, not different lines
        if letter in guessed_letters_list :
            print(letter, end = "")
        else :
            print("_", end = "")

# after every wrong guess, python tells you how many turns you have left
    print()
    print(f"you have {turns} tries left!!!")


# if guessed letters equals the random word, python prints congratulations

    if set(guessed_letters_list) == set(selected_word) :
         print()
         print("congatulation!!!")
         break
    


    

    # print(guessed_letters_list)