# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import random

words = ["bobnoonb", "worllldorq", "helloooooooeh"]
word = random.choice(words)
computer_word = list(word)
images = ["Hanged", "_____", "two", "Three", "Four","Five","All lives left"]


def main():
    """
    test function to print dashes for amount of letters in a word,
    take a user input and check if in the
    word the computer has chosen and print message accordingly
    """
    print("\n")
    user_choices = []
    lives = 6
    correct_guesses = []
    new_word = []
    for letters in word:
        print("_ ", end=" ")
    new_word = [char if char in correct_guesses else "_ " for char in word]
    while lives > 0 and len(computer_word) != 0:
        user_input = input("\nEnter a letter: ")
        if user_input in computer_word:
            print(f"Well Done {computer_word}")
            user_choices.append(user_input)
            while user_input in computer_word:
                correct_guesses.append(user_input)
                computer_word.remove(user_input)
            print(f"Correct letters : {correct_guesses}")
            print(f"user_choices are : {user_choices}")
            print(images[lives])
            new_word = [char if char in correct_guesses else "_ " for char in word]
            print("New Word: " + " ".join(new_word))
        else:
            print("Hard luck")
            user_choices.append(user_input)
            print(f"User_choices are {user_choices}")
            lives -= 1
            print(f"You have {lives} lives left")
            print("New Word: " + " ".join(new_word))
            print(images[lives])
    
    if len(computer_word) == 0:
        print("Winner")
        print("The word was : "+" ".join(new_word))
        print(images[lives])
    else:
        print("Game over")
        print("The Word was :" + word)
        print(images[lives])


main()
