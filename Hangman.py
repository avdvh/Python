import random

# List of words to choose from
word_list = ["python", "hangman", "programming", "computer", "keyboard", "developer"]  #Add as much word as you want as per your own requirement.

# Function to choose a random word from the list
def choose_word():
    return random.choice(word_list)

# Function to display the current state of the word
def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display

# Main Hangman game function
def hangman():
    word_to_guess = choose_word()
    guessed_letters = []
    attempts = 6

    print("Welcome to Hangman!")

    while True:
        display = display_word(word_to_guess, guessed_letters)
        print(f"Word: {display}")
        print(f"Attempts left: {attempts}")

        if "_" not in display:
            print("Congratulations! You guessed the word.")
            break

        if attempts == 0:
            print(f"Sorry, you're out of attempts. The word was '{word_to_guess}'.")
            break

        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess not in word_to_guess:
            attempts -= 1
            print("Wrong guess! Try again.")

if __name__ == "__main__":
    hangman()
