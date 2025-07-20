import random

def hangman():
    words = ["apple", "tiger", "plane", "watch", "chair"]
    word = random.choice(words)
    guessed_letters = []
    attempts = 6
    display_word = ["_" for _ in word]

    print("🎮 Welcome to Hangman!")
    print("Guess the word, one letter at a time.")
    print("You have", attempts, "wrong attempts allowed.\n")

    while attempts > 0 and "_" in display_word:
        print("Word:", " ".join(display_word))
        guess = input("Enter a letter: ").lower()

        if not guess.isalpha() or len(guess) != 1:
            print("❗ Please enter a single alphabet letter.\n")
            continue

        if guess in guessed_letters:
            print("⚠️ You already guessed that letter.\n")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print("✅ Correct!\n")
            for idx, letter in enumerate(word):
                if letter == guess:
                    display_word[idx] = guess
        else:
            attempts -= 1
            print(f"❌ Wrong guess! Attempts left: {attempts}\n")

    if "_" not in display_word:
        print("🎉 Congrats! You guessed the word:", word)
    else:
        print("💀 Game Over! The correct word was:", word)

hangman()
