import random

words = ["python", "apple", "chair", "table", "mouse"]
word = random.choice(words)

guessed = []
tries = 6

while tries > 0:
    display = ""
    for letter in word:
        if letter in guessed:
            display += letter
        else:
            display += "_"
    print("Word:", display)

    if display == word:
        print("You guessed the word!")
        break

    guess = input("Guess a letter: ")
    guessed.append(guess)

    if guess not in word:
        tries -= 1
        print("Wrong guess. Tries left:", tries)

if tries == 0:
    print("Game Over! Word was:", word)