def mask(saying):
    guessed_saying = ""
    for l in range(len(saying)):
        if saying[l] == " ":
            guessed_saying += " "
        else:
            guessed_saying += "#"
    return guessed_saying


class WheelOfFortune:

    def __init__(self, saying="I think so I am"):
        self.attempts: int = 0
        self.saying: str = saying
        self.guessed_saying: str = mask(saying)

    def guessed(self):
        return self.saying == self.guessed_saying

    def guess(self, letter):
        self.attempts += 1
        if letter.upper() in self.saying.upper():
            self.guessed_saying = self._recreate_guessed_saying(letter)

    def guess_saying(self, saying_guess):
        self.attempts += 1
        if saying_guess.upper() == self.saying.upper():
            self.guessed_saying = self.saying

    # private parts ------------------------------------------------------
    @staticmethod
    def _guessed(guessed_letter, saying_letter):
        return saying_letter.upper() == guessed_letter.upper() \
            or saying_letter.upper() == " "

    def _recreate_guessed_saying(self, letter):
        rebuild: str = ""
        for l in range(len(self.saying)):
            if self.saying[l] == " ":
                rebuild += " "
            elif self._guessed(letter, self.saying[l]):
                rebuild += self.saying[l]
            else:
                rebuild += self.guessed_saying[l]
        return rebuild
