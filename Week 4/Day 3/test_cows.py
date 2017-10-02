from cows_and_bulls import Game, Guess
import unittest

class TestGame(unittest.TestCase):
    def test_create_random_four_digit_num(self):
        self.assertTrue(len(str(Game().create_number())) == 4)        


class TestBuess(unittest.TestCase):
    def test_first_guess_counter_zero(self):
        self.assertTrue(Guess().guesses == 0)        
        


if __name__ == '__main__':
    unittest.main()
