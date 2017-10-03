# Anagram

# Create a function that takes two strings, 
# and returns a boolean that should be True if the strings are anagrams and False otherwise.

import unittest
import anagram

class TestAnagram(unittest.TestCase):

    def test_empty_string(self):
        self.assertTrue(anagram.is_anagram("", ""))

    def test_one_letter_false(self):
        self.assertFalse(anagram.is_anagram("a", "b"))
    
    def test_one_string_empty(self):
        self.assertFalse(anagram.is_anagram("", "b"))
        
    def test_letters_are_correct(self):
        self.assertTrue(anagram.is_anagram("a", "a"))

    def test_two_letter_string_anagram(self):
        self.assertTrue(anagram.is_anagram("ab", "ba"))
        
    def test_many_letter_anagram_true(self):
        self.assertTrue(anagram.is_anagram("abba", "baba"))

    def test_many_letter_anagram_false(self):
        self.assertFalse(anagram.is_anagram("acca", "baba"))

    def test_multiple_word_anagram_false(self):
        self.assertFalse(anagram.is_anagram("acca nekem a husit", "baba meken histu"))

    def test_multiple_word_anagram_true(self):
        self.assertTrue(anagram.is_anagram("acca   nekem a husit", "caca meken histau"))


if __name__ == "__main__":
    unittest.main()