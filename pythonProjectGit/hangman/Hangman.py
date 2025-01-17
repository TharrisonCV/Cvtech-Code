import random

# List of words to guess from
words = ["cat", "dog", "parrot", "elephant", "giraffe", "lion", "tiger", "bear", "zebra", "panda", "wolf", "fox", "rabbit", "koala", "kangaroo"]

# Randomly select a word from the list
answer = random.choice(words)


# Function to display the word with hidden letters
def display_word(word, guesses):
    return ' '.join(letter if letter in guesses else '_' for letter in word)


# Initialize a set to keep track of guessed letters
guessed_letters = set()

# Set the maximum number of incorrect guesses allowed
max_attempts = 6
max_word_attempts = 2
attempts = 0
word_attempts = 0

print("Welcome to the word guessing game!")
print(f"Guess the word. You have {max_attempts} attempts.")
print(f"Guess the word. You have {max_word_attempts} word attempts.")


# Main game loop
while attempts < max_attempts or word_attempts < max_word_attempts:
    # Display the current state of the word
    print("\nCurrent word: " + display_word(answer, guessed_letters))

    # Get user input
    guess = input("Guess a letter or the whole word: ").lower()

    # Validate the input
    if len(guess) == 1:
        if not guess.isalpha():
            print("Please enter a valid letter.")
            continue

        # Check if the letter has been guessed before
        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue

        # Add the guessed letter to the set of guessed letters
        guessed_letters.add(guess)

        # Check if the guessed letter is in the word
        if guess in answer:
            print("Good guess!")
        else:
            print("Incorrect guess.")
            attempts += 1

    elif len(guess) == len(answer):
        # If the guess is the same length as the answer, check if it's the whole word
        if guess == answer:
            print(f"Congratulations! You've guessed the word: {answer}")
            break
        else:
            print("Incorrect word guess.")
            word_attempts += 1

    else:
        print("Please enter a single letter or the full word.")

    # Check if the user has guessed the whole word
    if all(letter in guessed_letters for letter in answer):
        print(f"\nCongratulations! You've guessed the word: {answer}")
        break
else:
    # If the loop ends without breaking, the user has run out of attempts
    print(f"\nSorry, you've run out of attempts. The word was: {answer}")
