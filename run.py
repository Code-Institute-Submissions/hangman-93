"""
    Module that holds Functions for getting word from other modules,
    displaying word and playing Game
"""
import random
import re
import importlib
import os


CATEGORIES = ["words", "films", "books", "songs", "countries"]


def clear_screen():
    """
    Function to clear users screen depending on os
    ("clear" for posix (linux/Mac) otherwise "cls" is used for windows)
    """
    if os.name == 'posix':
        os.system('clear')
    else:
        os.system('cls')


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
    print("6. Choose 6 for the Computer to pick the Category")

    while True:
        category_choice = input("Pick a Category: \n")
        if (category_choice.isdigit() and int(category_choice) >= 1
                and int(category_choice) < 6):
            if int(category_choice) >= 1 and int(category_choice) < 6:
                selection = CATEGORIES[int(category_choice) - 1]
                module = importlib.import_module(selection)
                clear_screen()
                print(f"You have chosen: {selection.upper()}")
                print(module.STORY[0])
                input("Press Enter to continue...\n")
                return module
            if int(category_choice) == 6:
                selection = random.choice(CATEGORIES)
                module = importlib.import_module(selection)
                clear_screen()
                print(f"The Computer has chosen: {selection.upper()}")
                print(module.STORY[0])
                input("Press Enter to continue...\n")
                return module
        else:
            print("Sorry, that's not a vaild choice.")
            print("Please pick another category")
            continue


def difficulty_level():
    """
    Function to let the user choose difficulty, by setting the amount of
    lives they have
    """
    print("Choose your Difficulty Level")
    while True:
        print("Choose 'E' for Easy, 'M' for Medium or 'H' for Hard")
        print("(Easy = 10 lives, Medium = 8 Lives, Hard = 6 Lives)")
        difficulty = input("Difficulty: \n").upper()
        if difficulty.isalpha() and difficulty in {"E", "M", "H"}:
            if difficulty == "E":
                clear_screen()
                print("You have chosen: Easy")
                lives = 10
                input("Press Enter to continue...\n")
                return lives
            if difficulty == "M":
                clear_screen()
                print("You have chosen: Medium")
                lives = 8
                input("Press Enter to continue...\n")
                return lives
            if difficulty == "H":
                clear_screen()
                print("You have chosen: Hard")
                lives = 6
                input("Press Enter to continue...\n")
                return lives
        else:
            print("Sorry, that's not a vaild choice.")
            print("Please Choose either 'E', 'M' or 'H'")
            continue


def get_word():
    """
    Function to get a random word from the user picked category and also get
    the corresponding images, if the word contains spaces,
    the spaces are replaced with "-"'s
    """
    module = get_category_input()
    word = random.choice(module.CHOICES).upper()
    images = module.IMAGES
    story = module.STORY
    while any(not chr.isalpha() for chr in word):
        word = word.replace(" ", "-")
        return word, images, story
    return word, images, story


class Game:
    """
    Class that generates and displays computer
    choice of words and tests user input is valid
    """
    def __init__(self):
        self.word, self.images, self.story = get_word()
        self.computer_letters = list(self.word)
        self.lives = difficulty_level()
        self.user_choices = []
        self.correct_guesses = []

    def display_status(self):
        """
        Function to display game and word status to the user
        """
        print(f"Correct letters : {list(set(self.correct_guesses))}")
        print(f"Letters Picked Already : {self.user_choices}")
        if self.lives > 6:
            print(self.images[6])
        else:
            print(self.images[self.lives])
        print(f"You have {self.lives} lives left")
        new_word = [char if char in self.correct_guesses or not char.isalpha()
                    else "_ " for char in self.word]
        print(" ".join(new_word))

    def get_input(self):
        """
        Function to check if user input is a valid letter and if so return it
        in uppercase, if not ask for another letter
        """
        while True:
            self.display_status()
            guess = input("\nEnter a letter: \n").upper()
            if (guess.isalpha() and guess not in self.user_choices
                    and len(guess) == 1):
                clear_screen()
                self.user_choices.append(guess)
                return guess
            if guess.isalpha() and guess in self.user_choices:
                clear_screen()
                print("You've already picked that letter. Please try again.")
                continue
            if len(guess) > 1:
                clear_screen()
                print("Sorry, that's too many letters")
                continue
            clear_screen()
            print("That's not a letter! Please try again")
            continue

    def check_letters(self):
        """
        Check whether the user input is in the word and display accordingly
        """
        clear_screen()
        while (self.lives > 0 and len(self.computer_letters) != 0
                and re.search('[a-zA-Z]', str(self.computer_letters))):
            user_input = self.get_input()
            clear_screen()
            if user_input in self.computer_letters:
                while user_input in self.computer_letters:
                    self.correct_guesses.append(user_input)
                    self.computer_letters.remove(user_input)
                clear_screen()
                print(f"Well Done {user_input} was in the word!")
            else:
                clear_screen()
                print(f"Hard luck {user_input} was not in the word...")
                self.lives -= 1

    def replay(self):
        """
        Function to check if player wants to play again
        """
        replay = input("If you would like to play again, please press Y:\n")
        if replay.upper() == "Y":
            clear_screen()
            play = Game()
            play.check_letters()
            play.check_finished()
        else:
            clear_screen()
            main()

    def check_finished(self):
        """
        Check if the user has finished the game, either by guessing all
        letters or having no more lives
        """
        if not re.search('[a-zA-Z]', str(self.computer_letters)):
            print("Winner")
            print("The word was : "+" "+self.word)
            winner = importlib.import_module("ascii")
            print(winner.WINNER_ART)
            input("Press Enter to continue...\n")
            clear_screen()
            print(self.story[1])
            self.replay()

        else:
            print("Game over")
            print("The Word was :" + self.word)
            print(self.images[self.lives])
            input("Press Enter to continue...\n")
            clear_screen()
            print(self.story[2])
            self.replay()


def main():
    """
    Function to print dashes for amount of letters in a word,
    take a user input and check if it is in the
    word the computer has chosen and print message accordingly
    """
    introduction = importlib.import_module("ascii")
    print(introduction.INTRO)
    input("Press Enter to continue...\n")
    clear_screen()
    with open('rules.txt', encoding="utf-8") as file:
        rules = file.read()
    print(rules)
    input("Press Enter to continue...\n")
    clear_screen()
    play = Game()
    play.check_letters()
    play.check_finished()


if __name__ == "__main__":
    main()
