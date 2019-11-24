from unittest import TestCase
from WheelOfFortune import WheelOfFortune


class TestSayingWithSpaces(TestCase):
    def test_masked_saying_starts_out_fully_masked(self):
        self.wof = WheelOfFortune("abc de")
        self.assertEqual("### ##", self.wof.guessed_saying)

    def test_masked_saying_is_unmasked_when_all_letters_are_guessed(self):
        self.wof = WheelOfFortune("abc de")
        self.wof.guess("a")
        self.wof.guess("b")
        self.wof.guess("c")
        self.wof.guess("d")
        self.wof.guess("e")
        self.assertEqual("abc de", self.wof.guessed_saying)

    def test_masked_saying_stays_masked_if_guessing_wrong(self):
        self.wof = WheelOfFortune("abc de")
        self.wof.guess("b")
        self.assertEqual("#b# ##", self.wof.guessed_saying)

    def test_masked_saying_gets_unmasked_if_guessing_uppercase(self):
        self.wof = WheelOfFortune("abc de")
        self.wof.guess("B")
        self.assertEqual("#b# ##", self.wof.guessed_saying)

    def test_unmask_all_letters_that_were_guessed(self):
        self.wof = WheelOfFortune("abc abc")
        self.wof.guess("a")
        self.assertEqual("a## a##", self.wof.guessed_saying)

    def test_guess_unmasks_upper_and_lower_case(self):
        self.wof = WheelOfFortune("abc ABC")
        self.wof.guess("a")
        self.assertEqual("a## A##", self.wof.guessed_saying)

    def test_notice_that_the_saying_was_guessed(self):
        self.wof = WheelOfFortune("abc")
        self.assertFalse(self.wof.guessed())
        self.wof.guess("a")
        self.assertFalse(self.wof.guessed())
        self.wof.guess("b")
        self.assertFalse(self.wof.guessed())
        self.wof.guess("c")

        self.assertTrue(self.wof.guessed())

    def test_every_correct_guess_counts_as_an_attempts(self):
        self.wof = WheelOfFortune("abc")
        self.assertEqual(0, self.wof.attempts)
        self.wof.guess("a")
        self.assertEqual(1, self.wof.attempts)
        self.wof.guess("b")
        self.assertEqual(2, self.wof.attempts)
        self.wof.guess("c")
        self.assertEqual(3, self.wof.attempts)

    def test_every_incorrect_guess_counts_as_an_attempts(self):
        self.wof = WheelOfFortune("abc")
        self.assertEqual(0, self.wof.attempts)
        self.wof.guess("x")
        self.assertEqual(1, self.wof.attempts)
        self.wof.guess("y")
        self.assertEqual(2, self.wof.attempts)
        self.wof.guess("z")
        self.assertEqual(3, self.wof.attempts)

    def test_wrong_guess_saying_counts_as_an_attempt(self):
        self.wof = WheelOfFortune("abc")
        self.wof.guess_saying("123")
        self.assertFalse(self.wof.guessed())
        self.assertEqual(1, self.wof.attempts)

    def test_guess_saying_ignores_casing(self):
        self.wof = WheelOfFortune("abc")
        self.wof.guess_saying("ABC")
        self.assertTrue(self.wof.guessed())
        self.assertEqual(1, self.wof.attempts)
