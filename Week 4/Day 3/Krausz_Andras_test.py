from Krausz_Andras_work import Getting_apple, Sum
import unittest

class TestGetting_apple(unittest.TestCase):
    def test_get_apple(self):
        apple = Getting_apple()
        self.assertEqual(apple.get_apple(), "apple")


class TestSum(unittest.TestCase):
    def test_if_empty_list(self):
        self.assertEqual(Sum().sum_of_list([]), 0)

    def test_if_one(self):
        self.assertEqual(Sum().sum_of_list([1]), 1)

    def test_if_many(self):
        self.assertEqual(Sum().sum_of_list([1, 2, 3]), 6)

if __name__ == '__main__':
    unittest.main()