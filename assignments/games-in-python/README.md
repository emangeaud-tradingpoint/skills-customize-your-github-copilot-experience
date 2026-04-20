# 📘 Assignment: Games in Python

## 🎯 Objective

Build a simple Hangman game in Python to practice loops, conditionals, string manipulation, and user input. You will use starter code to create a playable program that selects a word, tracks guesses, and ends with a clear result.

## 📝 Tasks

### 🛠️	Set Up the Hangman Game

#### Description
Use the provided starter code to initialize the core game data. Your program should choose a secret word from the predefined list and prepare the variables needed to track guessed letters and remaining incorrect attempts.

#### Requirements
Completed program should:

- Randomly select a word from the provided `words` list.
- Create variables to store guessed letters and incorrect guesses.
- Set a maximum number of incorrect guesses allowed.
- Keep the code organized so the game is ready to enter the main loop.


### 🛠️	Build the Game Loop

#### Description
Complete the main Hangman gameplay loop so the player can keep guessing letters until they either reveal the full word or run out of attempts.

#### Requirements
Completed program should:

- Display the current word progress using underscores for letters that have not been guessed yet.
- Ask the player to enter one letter at a time.
- Update the game state based on whether the guessed letter is in the secret word.
- Decrease the remaining attempts when the guess is incorrect.
- End the game with a clear win message if the word is guessed.
- End the game with a clear lose message if the player uses all allowed incorrect guesses.
