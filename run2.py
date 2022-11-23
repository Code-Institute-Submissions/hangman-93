import random
from words import WORDS
from testwords import testwords

IMAGES = ["Hanged", "_____", "two", "Three", "Four", "Five", "All lives left"]


def get_word():
    """
    Function that gets computer to choose a random word
    """
   
    word = random.choice(testwords).upper()

    while any(not chr.isalpha() for chr in word):
        print(word)
        word = random.choice(testwords).upper()
    return word


class Game:
    """
    Class that generates and displays computer choice of words and tests user input is valid
    """
    def __init__(self):
        self.word = get_word()
        self.computer_word = list(self.word)
        self.lives = 6
        self.user_choices = []
        self.correct_guesses = []

    def get_input(self):
        """
        Function to check if user input is a valid letter and if so return it
        in uppercase, if not ask for another letter
        """
        while True:
            guess = input("\nEnter a letter: ").upper()
            
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
        new_word = [char if char in self.correct_guesses else "_ " for char in self.word]
        print()
        print(" ".join(new_word))

    def check_letters(self):
        """
        Check whether the user input is in the word and display accordingly
        """
        while self.lives > 0 and len(self.computer_word) != 0:
            user_input = self.get_input()
            if user_input in self.computer_word:
                print(f"Well Done {user_input} was in the word!")
                while user_input in self.computer_word:
                    self.correct_guesses.append(user_input)
                    self.computer_word.remove(user_input)
                print(f"Correct letters : {set(self.correct_guesses)}")
                print(f"User Choices are : {self.user_choices}")
                print(IMAGES[self.lives])
                self.display_word()
            else:
                print(f"\nHard luck {user_input} was not in the word...")
                print(f"User Choices are {self.user_choices}")
                self.lives -= 1
                print(f"You have {self.lives} lives left")
                self.display_word()
                print(IMAGES[self.lives])

    def check_finished(self):
        """
        Check if the user has finished the game, either by guessing all
        letters or having no more lives
        """
        if len(self.computer_word) == 0:
            print("Winner")
            print("The word was : "+" "+self.word)
            print(IMAGES[self.lives])
        else:
            print("Game over")
            print("The Word was :" + self.word)
            print(IMAGES[self.lives])


def main():
    """
    Function to print dashes for amount of letters in a word,
    take a user input and check if it is in the
    word the computer has chosen and print message accordingly
    """
    print("\nWelcome to Hangman! \nYou have 6 attempts to guess the correct letters in the word")
    play = Game()
    play.display_word()
    play.check_letters()
    play.check_finished()


main()
