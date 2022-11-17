# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import random

words = ["bobnoonb", "worllldorq", "helloooooooeh"]
computer_word = list(random.choice(words))


def main():
    """
    test function to print dashes for amount of letters in a word,
    take a user input and check if in the
    word the computer has chosen and print message accordingly
    """
    print("\n")
    user_choices = []
    lives = 5
    for letter in computer_word:
        print("_"+" ", end=" ")
    while lives > 0 and len(computer_word) > 0:
        user_input = input("Enter a letter: ")
        if user_input in computer_word:
            print(f"Well Done {computer_word}")
            user_choices.append(user_input)
            while user_input in computer_word:
                computer_word.remove(user_input)
                
            # If letter correct, remove it from list,
            # then if word list empty, player won
            
            print(f"user_choices are {user_choices}")
            print(f"Reduced word {computer_word}")
        else:
            print(f"Hard luck {computer_word}")
            user_choices.append(user_input)
            print(f"user_choices are {user_choices}")
            lives -= 1
            print(f"You have {lives} lives left")
    
    if len(computer_word) == 0:
        print("Winner")
    else:
        print("Game over")


main()
