import random

words = ["python", "github", "coding", "linux", "node"]

word = random.choice(words)

display = ["_"] * len(word)
attempts = 6

print("Welcome to Hangman!")

while attempts > 0 and "_" in display:

    print("\nWord:", " ".join(display))
    guess = input("Enter a letter: ").lower()

    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                display[i] = guess

        print("Correct!")
    else:
        attempts -= 1
        print("Nope, you made a wrong guess!")
        print("Attempts left:", attempts)

if "_" not in display:
    print("\n You Won!")
    print("The word was:", word)
else:
    print("No more attempts.. GAME OVER!")
    print("The word was:", word)