from words import franchises
import random

# Intro
print('Let\'s play Hangman')
print()

gameActive = True

remainingGuesses = 5

# Select random word from list
## Pick a random Index
randomIndex = random.randint(0, len(franchises)-1)
## Random Word
randomWord = franchises[randomIndex]

# Set player's view
playersView = []
wrongGuesses = []

for letter in randomWord:
    if letter == ' ':
        playersView.append(' ')
    else:
        playersView.append('_')

while gameActive == True:
    # Turn list into string for UX
    playerString = ''.join(playersView)

    # Check if game is still active
    if remainingGuesses == 0:
        print('You ran out of lives.')
        print(f'The word was {randomWord}')
        print('GAME OVER')
        gameActive = False
        break
    elif playerString == randomWord:
        print('You win!')
        print(f'You guesses {playerString} correctly!')
        gameActive = False
        break

    # UX
    print(playerString)

    # Let user know wrong guesses:
    ## Show if the player has guesses wrong
    if len(wrongGuesses) > 0:
        wrong = ' '.join(wrongGuesses)
        print(f'Wrong guesses: {wrong}')

    # Ask player to guess a letter
    playerGuess = str(input('Please guess a letter: '))

    # UX to make the game look cleaner
    print()
    print('_____________________________________________________')
    print(f'Remaining guesses: {remainingGuesses}')

    # Check if player's guess is in randomWord
    if playerGuess.lower() in playerString.lower():
        print(f'YOU ALREADY ASKED {playerGuess} AND IT WAS RIGHT')
    for guess in range(len(randomWord)):
        if randomWord[guess].lower() == playerGuess.lower():
            playersView[guess] = randomWord[guess]

    # If guess not in randomWord add to wrong list
    if playerGuess.lower() not in randomWord.lower():
        if playerGuess.lower() in wrongGuesses:
            print(f'YOU ALREADY ASKED {playerGuess} AND IT WAS WRONG')
        else:
            # Subtract one remaining guess
            remainingGuesses -= 1
            # Add letter to wrongGuesses list
            wrongGuesses.append(playerGuess.lower())







