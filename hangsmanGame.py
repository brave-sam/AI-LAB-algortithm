import random

def choose_word():
    word_list = ["apple", "banana", "orange", "grape", "pineapple", "watermelon", "strawberry"]
    return random.choice(word_list)

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    return display

def hangman():
    secret_word = choose_word()
    guessed_letters = []
    attempts = 6

    print("Welcome to Hangman!")
    print(display_word(secret_word, guessed_letters))

    while attempts > 0:
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single alphabetical character.")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess not in secret_word:
            attempts -= 1
            print(f"Wrong guess! Attempts left: {attempts}")
        
        print(display_word(secret_word, guessed_letters))

        if "_" not in display_word(secret_word, guessed_letters):
            print("Congratulations! You've guessed the word!")
            break

    if "_" in display_word(secret_word, guessed_letters):
        print(f"Out of attempts! The word was '{secret_word}'.")

hangman()
