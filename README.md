
<h1>Welcome to HANGMAN</h1>

This is a Python terminal version of [Hangman](https://forgottenit-hangman.herokuapp.com). It runs in the Code Institute mock terminal. 

The User is given a certain amount of attempts to try guess letters in a hidden word picked by the computer.

You can read more about Hangman on [Wikipedia](https://en.wikipedia.org/wiki/Hangman_(game))

## How to Play

* At the Loading screen the User is asked to press Enter, then thr rules are displayed
* The user is asked to choose a category, these are either : Words, Songs (Singles), Films, Books or Countries. Or the user can let the computer pick the category.
* The user is then shown the background story for their category. The user then decides if they want to play Easy (10 lives), Medium (8 lives) or Hard (6 lives)
* The Computer picks a word from the chosen category and displays blanks (_'s) to the user to signify the amount of letters in the word. If the word contains symbols such as hyphens or numbers (1,2,3 etc.) These are displayed to the user. If it's roman numerals (i.e. I or V etc.) These are not displayed. 
* The User is then asked to try guess a letter that is in the word. The input will only allow lettera to be attempted. It also will tell the user if they've already attempted the letter.
* If the User's guess is in the word, the computer displays the letter (or letters if there are multiple instances of the letter) in place of the blanks. If it is not in the word, the user loses a life.
* Lives are only reduced for incorrect answers, not for reguessing the same input or inputting invalid input (i.e. numbers)
* The User keeps guessing until they have guessed all the correct letters (They win) or runs out of lives/attempts (They lose)
* After the game they are shown the corresponding End story, and asked if they want to play again, if they enter "Y" the game reverts back to the category choice, any other input leads back to the intro image


## Flow Chart for Hangman

<img src="Docs/Flowchart.png">

## Design

* The Intro Art is to display to the User the Game, ASCII Art was used for visual appeal.

<img src="Docs/intro.png">

* Rules are then displayed to the user to explain how the game will work.

<img src="Docs/rules.png">

* Categories are then offered to the user to pick from, the user can also have the computer select the category, this is so the user will know where the word comes from i.e. Film titles, Book titles etc. to add some variety to the game.

<img src="Docs/categories.png">

* Each Category has its own introduction and end story, this is to add a bit more fun for the user and variety.

<img src="Docs/story1.png">

* Each Category in the game has its own ASCII Art relative to the category, Random words is the typical Hangman image, Countries is a picture of the Earth, Songs is music notes etc. Again, this is to add variety and replayability. The Blanks are also spaced out so the user can see how many letters the word contains and the remaining lives are also displayed.

<img src="Docs/game.png">

* The Game displays a message to you user saying they guessed correctly and also the letter in it's correct place, replacing the underscore. It also displays to the user the letters they've already picked and which ones were correct.

<img src="Docs/correct_letter.png">   

* The Game displays a message once an incorrect letter is inputted, saying this was incorrect and adds that letter to the list of letters the player has already picked. 

<img src="Docs/incorrect.png">

* If the player Guesses the correct word a trophy is displayed to the User using ASCII Art.

<img src="Docs/winner.png">

* The player is then shown the end of the category Story, dependent on the category they chose and how they did. If they failed to get the word, they are given a different story. They are then asked if they would like to play again, if so (By Entering y) they go back to Category selection, everything else brings them back to the intro screen.

<img src="Docs/end.png">


## Technology used

1. GitPod for writing the code
2. Python as the programming language
3. Heroku for deployment
4. Code Instistute Terminal for displaying finished product
5. https://pep8ci.herokuapp.com/ CI Python Linter for testing code

## Imports used from Python Library
* import random - Used to allow the computer to randomly pick a category if that is the choice the user has made and also to randomly pick the word from choices available
* import re - Used to search the word as a string to see if it still contains letters (in case it just contains characters or numbers)
* import importlib - Used to import modules dynamically, once the user has chosen their category
* import os - Used for the "Clear Screen" function, to check what Operating System the user is using so the appropriate clear method can be used (i.e. "clear" or "cls")

## Testing

1. Testing involved using pylint on all the .py modules by running pylint in the terminal, where all code reached 10 out of 10.

<img src="Docs/pylint.png">

2. Testing also involved [CI Python Linter](https://pep8ci.herokuapp.com/) with Results returning All Clear, no errors found.

<img src="Docs/CI_pep8.png">

3. Testing also involved Practical testing, this was ongoing throughout the project, both in the Terminal and then on the deployed app. This was to ensure all the input gave the expected results, the links worked, that it deployed correctly on the Code Institute Terminal etc. Testing also involved ensuring that symbols (i.e. commas, apostrophes, hyphens etc.) were displayed to the user. Also, ensuring that if the correct letter was entered, all instances of the letter were filled in. All letters are converted to uppercase also, so the game is not case sensitive. Also, only one letter of input is taken at a time in the game, if the user enters more than that, they are given a display message to indicate that. Testing also checked that lives are only reduced for incorrect answers, not for reguessing the same input or inputting invalid input (i.e. numbers)


- In Categories, if the user does not enter a valid input (a number between 1 and 6 inclusive) an error message is displayed.

<img src="Docs/errors1.png">


- In Difficulty Settings, if the user does not enter a valid input ("E" for Easy, "M" for Medium, "H" for Hard) an error message is displayed and they are asked again for input

<img src="Docs/errors2.png">


- If the user inputs a number or symbol or a blank, the terminal displays that it wasn't a valid input (No lives are lost). A separate message is displayed if the letter was guessed already or if the user has inputted too many characters (Again, no lives are lost in these instances)

<img src="Docs/error3.png">   <img src="Docs/already_picked.png">


## Constraints

* The deployment terminal is set to 80 columns by 24 rows. That means that each line of text needs to be 80 characters or less otherwise it will be wrapped onto a second line.
* A "\n" symbol had to be inserted at the end if user input print outs due to a quirk in the terminal interface.

# Learning and Future Improvements

## Learning

* When initially deploying the App, I had used the import from method to get the words (i.e. import books, import songs etc.) This would involve writing if input == "something" word == "something" for each category choice, as I couldn't find a way to import dynamically using this (i.e. import {user_input}) So I used the importlib to acheive this, as I felt it minimised the code needed as I could just use a list index for the user input. However, this did mean that I had to name the variables in each category module the same (CHOICES, IMAGES, STORY). So it would be books.IMAGES or songs.IMAGES etc. 

* I found using sets to be helpful in displaying correct choices, as if there was more than one instance of the letter, it would only display it once in the users list. I did convert the display to a list though for consistency of display. 

## Future improvements  

* Originally, to have variety in the game, I wanted to include Movies, Books etc. and because these often included spaces, hyphens etc. I felt it best to just take alphabetical input. This limited the game in that the user could not just outright guess the word. I felt it might be messy as the user may input the apostrophes, spaces etc. 

* Though it would have been possible to use the strip() method etc. to remove spaces and just check the letters inputted against the word, as the user only loses lives for incorrect answers, if they had the word they could still play by entering the letters one at a time. So this functionality was omitted. But may still have improved the game.

* Another improvement would be to import json files, from an API for example, and use the Keys for hints. For example, a Book file may have author, year, type etc. The user could type in "hint" and one of these could be displayed, possibly for a limited amount of time using the sleep() function. Or the user could select what hint they would like i.e. 1. for Author, 2. for Genre 3. for Year etc. This would work for Songs, Films etc. as well, or if words were taken from an actual dictionary, the definition could be displayed (using the hidden word as the key). 

* Also the Art could be improved, perhaps by having multiple images displayed to give it a moving effect using a time delay between images that have slight alterations. 


## Deployment
<h3>GitPod<h3>

* To deploy [Hangman](https://github.com/Forgottenit/hangman) in GitPod load from the GitHub repository, then enter "Python3 run.py" in the main terminal on GitPod

<h3>Heroku</h3>
1. Go to the Heroku Dashboard and Click "New" in the top right corner then click "Create new app"

  <img src="Docs/Home.png">

2. Name the App and set the region to Europe

  <img src="Docs/App%20Information.png">

3. Go to Settings and, Click Reveal Config Vars and set keys to PORT and value to 8000

  <img src="Docs/VARS.png">

4. Click Add Buildpacks, add Python, save changes.

  <img src="Docs/Buildpacks1.png">

  <img src="Docs/Buildpacks2.png">

5. Repeat step 4, but this time add Node.js, once completed it should look like below, with heroku/python above herokue/node.js, if now they can be clicked upon and dragged to change to this order.

  <img src="Docs/Completed%20Buildpacks.png">

6. Navigate to the Deploy section. Select GitHub from the Deployment Method section, connnect your GitHub Repo by selecting the repo name (in this case, hangman) and Authorise when prompted.

  <img src="Docs/Deploy%20menu.png">

  <img src="Docs/Deployment%20Method.png">

  <img src="Docs/Connect%20to%20Github.png">

7. Click Enable Automatic Deploys. Once Changes are pushed to your repo, the app will be constucted.

  <img src="Docs/Automatic%20Deploys.png">

8. Finally, click Open App to run the App in the Code Institute Terminal

  <img src="Docs/Open%20App.png">

9. [Hangman](https://forgottenit-hangman.herokuapp.com) is available by clicking this link.

## Acknowledgements 
* https://wtools.io/convert-list-to-json-array for converting lists to json format
* https://www.britannica.com/topic/list-of-countries-1993160 for list of countries
* https://www.theguardian.com/news/datablog/2012/nov/04/uk-million-selling-singles-full-list#data for song list
* https://en.wikipedia.org/wiki/AFI%27s_100_Years...100_Movies for film list
* https://www.randomlists.com/ for random list of words
* https://en.wikipedia.org/wiki/List_of_best-selling_books for list of books
* https://www.scaler.com/topics/how-to-clear-screen-in-python/ for info on how to Clear User Screen depending 
  on operating System
* https://codebeautify.org/ for Formatting lists 
* https://emojicombos.com/ AND https://asciiflow.com/ for ASCII Art
* https://stackoverflow.com/ AND https://docs.python.org/ for general python queries
* Simen Daehlin and Rohit Sharma from Code Institute for advice and guidance
* Code Instititute for learning materials and instructions on deployment
* Shizuka Donaghue (Code Institute Student) for assistance with Heroku deployment
