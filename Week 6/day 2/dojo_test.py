import unittest
import dojo

class TestPoker(unittest.TestCase):

    def test_empty_hands(self):
        self.poker = dojo.Poker()
        self.assertEqual(self.poker.hands_dealt([]), "No hands dealt.")

    def test_high_card(self):
        self.poker = dojo.Poker()
        self.assertEqual(self.poker.high_card([['D2', 'C3', 'H5', 'ST', 'DA'], ['D7', 'S3', 'H4', 'DT', 'DK']]), 'First hand wins, with high card')

    def test_if_not_first_highest_card_wins(self):
        self.poker = dojo.Poker()
        self.assertEqual(self.poker.high_card([['D2', 'C3', 'H5', 'ST', 'DA'], ['D7', 'S3', 'H4', 'DT', 'DA']]), 'Second hand wins, with high card')

if __name__ == "__main__":
    unittest.main()