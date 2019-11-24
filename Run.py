from WheelOfFortune import WheelOfFortune
from ConsoleInteraction import *

if __name__ == '__main__':

    wof = WheelOfFortune()
    print("Welcome to wheel of fortune")
    print("#@#@#@#@#@#@#@#@#@#@#@#@#@#")
    print()
    print("Guess our saying, letter by letter")
    print("or enter / to guess the full saying")
    print("___________________________________")
    while not wof.guessed():
        guess = ask_guess("{0} -> Guess {1:00}: ".format(wof.guessed_saying, wof.attempts + 1))
        if guess == '/':
            wof.guess_saying(input("Guess the whole saying : "))
        else:
            wof.guess(guess)

    print(wof.guessed_saying, " -> ", end="")
    print("you made it in {} attempts".format(wof.attempts))
