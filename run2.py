import random

words = ["bobnoonb", "worllldorq", "helloooooooeh"]
user_choices = []
correct_guesses = []
images = ["Hanged", "_____", "two", "Three", "Four", "Five", "All lives left"]


class Game:
    """
    Class that generates and displays computer choice of words and tests user input is valid
    """
    def __init__(self):
        self.word = random.choice(words).upper()
        self.computer_word = list(self.word)
        self.lives = 6

    def get_input(self):
        """
        Function to check if user input is a valid letter and if so return it
        in uppercase, if not ask for another letter
        """
        while True:
            guess = input("\nEnter a letter: ").upper()
            
            if guess.isalpha() and guess not in user_choices and len(guess) == 1:
                user_choices.append(guess)
                return guess
            elif guess.isalpha() and guess in user_choices:
                print("You've already picked that letter. Please try again.")
                print(f"Correct letters : {set(correct_guesses)}")
                print(f"user_choices are : {user_choices}")
                continue
            elif len(guess) > 1:
                print("Sorry, that's too many letters")
                continue
            else:
                print("That's not a letter! Please try again")
                print(f"Correct letters : {set(correct_guesses)}")
                print(f"user_choices are : {user_choices}")
                continue

    def display_word(self):
        """
        Function to display hidden word in a line of dashes
        """
        new_word = [char if char in correct_guesses else "_ " for char in self.word]
        print()
        print(" ".join(new_word))

    def check_finished(self):
        if len(self.computer_word) == 0:
            print("Winner")
            print("The word was : "+" "+self.word)
            print(images[self.lives])
        else:
            print("Game over")
            print("The Word was :" + self.word)
            print(images[self.lives])


def main():
    """
    Function to print dashes for amount of letters in a word,
    take a user input and check if it is in the
    word the computer has chosen and print message accordingly
    """
    print("\nWelcome to Hangman! \nYou have 6 attempts to guess the correct letters in the word")
    play = Game()
    play.display_word()
    
    while play.lives > 0 and len(play.computer_word) != 0:
        user_input = play.get_input()
        if user_input in play.computer_word:
            print(f"Well Done {user_input} was in the word!")
            while user_input in play.computer_word:
                correct_guesses.append(user_input)
                play.computer_word.remove(user_input)
            print(f"Correct letters : {set(correct_guesses)}")
            print(f"User Choices are : {user_choices}")
            print(images[play.lives])
            play.display_word()
        else:
            print(f"\nHard luck {user_input} was not in the word...")
            print(f"User Choices are {user_choices}")
            play.lives -= 1
            print(f"You have {play.lives} lives left")
            play.display_word()
            print(images[play.lives])
    play.check_finished()
   

main()
