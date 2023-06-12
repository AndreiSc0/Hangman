import time

name = input("What is your name? ")
print(f"Hello, {name}. Time to play hangman!")
time.sleep(0.5)

word = "StarWars".lower()
guesses = ''
turns = 10

while turns > 0:
    failed = 0
    for char in word:
        if char in guesses:
            print(char, end="")
        else:
            print(" ", end="")
            failed += 1
    if failed == 0:
        print("\nYou Won!")
        break

    guess = input("\nGuess a character: ")
    if guess in guesses:
        print("You already guessed that letter.")
        continue

    guesses += guess

    if guess not in word:
        turns -= 1
        print("Bad Choice!")
        print(f"You have {turns} more guesses.")
        if turns == 0:
            print("Game Over. You Lose!")