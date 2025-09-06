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
    #print("Guessed letters:", " ".join(sorted(guessed_letters)))
    print()


def play_game():
    while True:
        secret_word = get_random_word()
        guessed_letters = set()
        mistakes = 0
        max_mistakes = len(ascii_art.STAGES) - 1

        print("Welcome to Snowman Meltdown!")

        while mistakes < max_mistakes:
            display_game_state(mistakes, secret_word, guessed_letters)

            # Input Validation
            while True:
                guess = input("Guess a letter: ").lower()
                if len(guess) != 1 or not guess.isalpha():
                    mistakes += 1
                    display_game_state(mistakes, secret_word, guessed_letters)
                    print(f"Please enter just one alphabetical character. Mistakes: {mistakes}/{max_mistakes}\n")
                    if mistakes >= max_mistakes:
                        break
                    continue
                break

            if mistakes >= max_mistakes:
                print(f"Game Over! The snowman melted. The word was: {secret_word}")
                break  # Stop the main loop to prevent IndexError

            # Check for duplicate guesses
            if guess in guessed_letters:
                print(f"You already guessed '{guess}'. Try another letter.\n")
                continue

            print("You guessed:", guess)
            guessed_letters.add(guess)

            # Handling for incorrect guesses
            if guess not in secret_word:
                mistakes += 1
                print(f"Wrong guess! '{guess}' is not in the word. Mistakes: {mistakes}/{max_mistakes}")

            # Check for win
            if all(letter in guessed_letters for letter in secret_word):
                display_game_state(mistakes, secret_word, guessed_letters)
                print("Congratulations! You saved the snowman!")
                break

        else:
            # Lost Game
            display_game_state(mistakes, secret_word, guessed_letters)
            print(f"Game Over! The snowman melted. The word was: {secret_word}")

        play_again = input("Do you want to play again? (y/n): ").lower()
        if play_again != "y":
            break
