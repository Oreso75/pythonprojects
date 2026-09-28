HANGMAN_PICTURES = [
    """
    _________________
    |               |
    |
    |
    |
    |
    |
    |
    |________________
    """,
    """
    _________________
    |               |
    |               O
    |
    |
    |
    |
    |
    |________________
    """,
    """
    _________________
    |               |
    |               O
    |               |
    |
    |
    |
    |
    |________________
    """,
    """
    _________________
    |               |
    |               O
    |              /|
    |
    |
    |
    |
    |________________
    """,
    """
    _________________
    |               |
    |               O
    |              /|\\
    |
    |
    |
    |
    |________________
    """,
    """
    _________________
    |               |
    |               O
    |              /|\\
    |              /
    |
    |
    |
    |________________
    """,
    """
    _________________
    |               |
    |               O
    |              /|\\
    |              / \\
    |
    |
    |
    |________________
    """,
]


print("Welcome To Sam's Hangman!")
secret_word = input("Player 1, Type your secret word: ").strip().lower()

while not secret_word or not any(letter.isalpha() for letter in secret_word):
    print("Please type a word with at least one letter.")
    secret_word = input("Player 1, Type your secret word: ").strip().lower()

word_display = []
for letter in secret_word:
    if letter.isalpha():
        word_display.append("_")
    else:
        word_display.append(letter)

guessed_letters = []
wrong_guesses = 0
max_wrong_guesses = len(HANGMAN_PICTURES) - 1

print("\n" * 40)
print("The game begins!")

while wrong_guesses < max_wrong_guesses and "_" in word_display:
    print(HANGMAN_PICTURES[wrong_guesses])
    print("Secret Word:                 Your Guesses:")
    print(" ".join(word_display), " " * 12, " ".join(guessed_letters))
    print(f"Wrong guesses left: {max_wrong_guesses - wrong_guesses}")

    guess = input("Guess Letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please guess one letter.\n")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.\n")
        continue

    guessed_letters.append(guess)

    if guess in secret_word:
        for i, letter in enumerate(secret_word):
            if letter == guess:
                word_display[i] = guess
        print("Good guess!\n")
    else:
        wrong_guesses += 1
        print("Nope, that letter is not in the word.\n")

print(HANGMAN_PICTURES[wrong_guesses])

if "_" not in word_display:
    print("You win!")
    print("The word was:", secret_word)
else:
    print("Game over!")
    print("The word was:", secret_word)
