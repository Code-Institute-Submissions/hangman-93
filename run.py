# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import random

words = ["bobnoonb", "worllldorq", "helloooooooeh"]
word = random.choice(words).upper()
computer_word = list(word)
images = ["Hanged", "_____", "two", "Three", "Four", "Five", "All lives left"]
user_choices = []
correct_guesses = []


def get_input():
    """
    Function to check if user input is a valid letter and if so return it
    in uppercase, if not ask for another letter
    """
    while True:
        guess = input("\nEnter a letter: ").upper()
        if guess.isalpha() and guess not in user_choices:
            user_choices.append(guess)
            return guess
        elif guess.isalpha() and guess in user_choices:
            print("You've already picked that letter. Please try again.")
            print(f"Correct letters : {set(correct_guesses)}")
            print(f"user_choices are : {user_choices}")
            continue
        else:
            print("That's not a letter! Please try again")
            print(f"Correct letters : {set(correct_guesses)}")
            print(f"user_choices are : {user_choices}")
            continue


def main():
    """
    Function to print dashes for amount of letters in a word,
    take a user input and check if it is in the
    word the computer has chosen and print message accordingly
    """
    print("\nWelcome to Hangman! \nYou have 6 attempts to guess the write letters in the word")
    lives = 6
    new_word = [char if char in correct_guesses else "_ " for char in word]
    print()
    print(" ".join(new_word))
    while lives > 0 and len(computer_word) != 0:
        user_input = get_input()
        if user_input in computer_word:
            print(f"Well Done {user_input} was in the word!")
            while user_input in computer_word:
                correct_guesses.append(user_input)
                computer_word.remove(user_input)
            print(f"Correct letters : {set(correct_guesses)}")
            print(f"User Choices are : {user_choices}")
            print(images[lives])
            new_word = [char if char in correct_guesses else "_ " for char in word]
            print("New Word: " + " ".join(new_word))
        else:
            print(f"Hard luck {user_input} was not in the word...")
            print(f"User Choices are {user_choices}")
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
