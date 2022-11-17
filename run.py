# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import random

words = ["bob", "world", "hellooooooo"]
computer_word = list(random.choice(words))


def main():
    """
    test function to print dashes for amount of letters in a word,
    take a user input and check if in the
    word the computer has chosen and print message accordingly
    """
    print()
    for letter in computer_word:
        print("_"+" ", end=" ")
    user_choices = []
    user_input = input("Enter a letter: ")
    user_choices.append(user_input)
    if user_input in computer_word:
        print(f"Well Done {computer_word}")
        print(user_choices)
    else:
        print(f"Well Done {computer_word}")
        print(user_choices)
        

main()
