import random
import re
import importlib


categories = ["words", "films", "books", "songs", "countries"]


def get_category_input():
    """
        Function to display category choices to user and return their choice
    """
    print("You can choose what category you would like your word from:")
    print("1. Choose 1 for Random Words")
    print("2. Choose 2 for Film titles")
    print("3. Choose 3 for Book titles")
    print("4. Choose 4 for Music Singles titles")
    print("5. Choose 5 for Countries")
    print("6. Choose 6 to let the computer pick")
    category_choice = input("Pick a Category: \n")
    return category_choice


def get_category():
    """
    Function that imports the category the user has picked and return the value
    """
    while True:
        category_choice = get_category_input()
        if category_choice.isdigit() and int(category_choice) >= 1 and int(category_choice) < 6:
            selection = categories[int(category_choice) - 1]
            module = importlib.import_module(selection)
            print(f"You have chosen: {selection}")
            return module
        elif int(category_choice) == 6:
            selection = random.choice(categories)
            module = importlib.import_module(selection)
            print(f"The Computer has chosen: {selection}")
            return module
        else:
            print("Sorry, that's not a vaild choice.")
            print("Please pick another category")
            continue


def get_word():
    """
    Function to get a random word from the user picked category and also get the corresponding images, 
    if the word contains spaces, the spaces are replaced with "-"'s
    """
    module = get_category()
    word = random.choice(module.choices).upper()
    images = module.IMAGES
    while any(not chr.isalpha() for chr in word):
        word = word.replace(" ", "-")
        return word, images
    return word, images


class Game:
    """
    Class that generates and displays computer
    choice of words and tests user input is valid
    """
    def __init__(self):
        self.word, self.images = get_word()
        self.computer_letters = list(self.word)
        self.lives = 6
        self.user_choices = []
        self.correct_guesses = []

    def get_input(self):
        """
        Function to check if user input is a valid letter and if so return it
        in uppercase, if not ask for another letter
        """
        while True:
            guess = input("\nEnter a letter: \n").upper()

            if guess.isalpha() and guess not in self.user_choices and len(guess) == 1:
                self.user_choices.append(guess)
                return guess
            elif guess.isalpha() and guess in self.user_choices:
                print("You've already picked that letter. Please try again.")
                print(f"Correct letters : {set(self.correct_guesses)}")
                print(f"user_choices are : {self.user_choices}")
                continue
            elif len(guess) > 1:
                print("Sorry, that's too many letters")
                continue
            else:
                print("That's not a letter! Please try again")
                print(f"Correct letters : {set(self.correct_guesses)}")
                print(f"user_choices are : {self.user_choices}")
                continue

    def display_word(self):
        """
        Function to display hidden word in a line of dashes
        """
        new_word = [char if char in self.correct_guesses or not char.isalpha() else "_ " for char in self.word]
        print()
        print(" ".join(new_word))

    def check_letters(self):
        """
        Check whether the user input is in the word and display accordingly
        """
        while self.lives > 0 and len(self.computer_letters) != 0 and re.search('[a-zA-Z]', str(self.computer_letters)):
            user_input = self.get_input()
            if user_input in self.computer_letters:
                print(f"Well Done {user_input} was in the word!")
                while user_input in self.computer_letters:
                    self.correct_guesses.append(user_input)
                    self.computer_letters.remove(user_input)
                print(f"Correct letters : {set(self.correct_guesses)}")
                print(f"User Choices are : {self.user_choices}")
                print(self.images[self.lives])
                self.display_word()
            else:
                print(f"\nHard luck {user_input} was not in the word...")
                print(f"User Choices are {self.user_choices}")
                self.lives -= 1
                print(f"You have {self.lives} lives left")
                self.display_word()
                print(self.images[self.lives])

    def check_finished(self):
        """
        Check if the user has finished the game, either by guessing all
        letters or having no more lives
        """
        if not re.search('[a-zA-Z]', str(self.computer_letters)):
            print("Winner")
            print("The word was : "+" "+self.word)
            print(self.images[self.lives])
        else:
            print("Game over")
            print("The Word was :" + self.word)
            print(self.images[self.lives])


def main():
    """
    Function to print dashes for amount of letters in a word,
    take a user input and check if it is in the
    word the computer has chosen and print message accordingly
    """
    print("\nWelcome to Hangman!")
    print("\nYou have 6 attempts to guess the correct letters in the word")
    play = Game()
    play.display_word()
    play.check_letters()
    play.check_finished()


if __name__ == "__main__":
    main()
