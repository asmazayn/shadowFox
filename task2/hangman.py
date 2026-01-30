import random

# ---------------- GAME SETUP ----------------
words = ["python", "cyber", "network", "shadow", "security"]
secret_word = random.choice(words)

guessed_letters = []
wrong_guesses = 0
max_attempts = 6

# Hangman visual stages
hangman_stages = [
    """
     -----
     |   |
         |
         |
         |
         |
    --------
    """,
    """
     -----
     |   |
     O   |
         |
         |
         |
    --------
    """,
    """
     -----
     |   |
     O   |
     |   |
         |
         |
    --------
    """,
    """
     -----
     |   |
     O   |
    /|   |
         |
         |
    --------
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
         |
         |
    --------
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
    /    |
         |
    --------
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
    / \\  |
         |
    --------
    """
]

print("🎮 Welcome to Hangman!")

# ---------------- GAME LOOP ----------------
while wrong_guesses < max_attempts:

    # -------- DISPLAY INTERFACE --------
    display_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print(hangman_stages[wrong_guesses])
    print("Word:", display_word)

    # -------- WIN CONDITION --------
    if "_" not in display_word:
        print("🎉 Congratulations! You guessed the word:", secret_word)
        break

    # -------- USER INPUT --------
    guess = input("Guess a letter: ").lower()

    # -------- INPUT VALIDATION --------
    if not guess.isalpha() or len(guess) != 1:
        print("⚠ Please enter a single alphabet letter.")
        continue

    if guess in guessed_letters:
        print("⚠ You already guessed this letter.")
        continue

    guessed_letters.append(guess)

    # -------- CHECK GUESS --------
    if guess not in secret_word:
        wrong_guesses += 1
        print("❌ Wrong guess! Attempts left:", max_attempts - wrong_guesses)
    else:
        print("✅ Correct guess!")

# ---------------- LOSS CONDITION ----------------
if wrong_guesses == max_attempts:
    print(hangman_stages[wrong_guesses])
    print("💀 Game Over! The word was:", secret_word)
