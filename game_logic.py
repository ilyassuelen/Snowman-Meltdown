import random
import ascii_art

# List of secret words
WORDS = ["python", "git", "github", "snowman", "meltdown"]

def get_random_word():
    """Selects a random word from the list."""
    return random.choice(WORDS)


def display_game_state(mistakes, secret_word, guessed_letters):
    """Displays the current snowman stage and the word with guessed letters."""
    print(ascii_art.STAGES[mistakes])  # Show current snowman stage

    # Show secret word with guessed letters revealed
    display_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "
    print("Word: ", display_word.strip())
    print("Guessed letters:", " ".join(sorted(guessed_letters)))
    print()


def play_game():
    secret_word = get_random_word()
    guessed_letters = set()
    mistakes = 0

    print("Welcome to Snowman Meltdown!")
    display_game_state(mistakes, secret_word, guessed_letters)
    print("Secret word selected: " + secret_word)  # for testing, later remove this line

    # Prompt user for one guess (logic to be enhanced later)
    guess = input("Guess a letter: ").lower()
    print("You guessed:", guess)
