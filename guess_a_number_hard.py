from random import randint as r

title = "Random Number Guesser"


def getRandom(maximum: int):
    return r(0, maximum)


print(f"$----- Welcome to {title}! -----$\n--- Guess a number! ---\n")

while True:

    try:
        guess: int = eval(input(""))

        if type(guess) == float:
            raise BaseException

    except ValueError | SyntaxError | BaseException:
        print("--- Please enter a number. ---")
        continue

    number: int = getRandom(100)
    guesses: int = 0

    while True:
        if guesses == 10:
            print(f"--- You guessed too many times! ---")
            break

        if 0 < guess > 100:
            print("--- Please enter a number between 0 and 100. ---\n")

        if guess == number:
            print(f"----- You guessed the number in {guesses} guesses! -----\n")
            break

        elif number > guess:
            print(f"--- Your guess is too low! ---\n")
            guesses += 1

        elif guess > number:
            print(f"--- Your guess is too high! ---\n")
            guesses += 1

        else:
            print(f"--- Something went wrong. ---\n")

        try:
            guess: int = int(input(""))

        except ValueError:
            print("--- Please enter a number. ---")
