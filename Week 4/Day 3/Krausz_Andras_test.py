from Krausz_Andras_work import Getting_apple, Sum, Anagram, Count_letters, Fibonacci
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


class TestAnagram(unittest.TestCase):
    def test_anagrama_if_true(self):
        self.assertTrue(Anagram().anagram("indulagörögaludni"))

    def test_anagrama_if_true(self):
        self.assertFalse(Anagram().anagram("mylittlepony"))
        
        
class TestCount_letters(unittest.TestCase):
    def test_if_empty(self):
        count = Count_letters()
        self.assertEqual(count.count_letters(""), {})
    
    def test_if_one(self):
        count = Count_letters()
        self.assertEqual(count.count_letters("a"), {"a": 1})        

    def test_if_many(self):
        count = Count_letters()
        self.assertEqual(count.count_letters("ab"), {"a": 1, "b": 1})        

    def test_if_double(self):
        count = Count_letters()
        self.assertEqual(count.count_letters("aa"), {"a": 2})        


class TestFibonacci(unittest.TestCase):
    def test_if_one(self):
        self.assertEqual(Fibonacci().fibonacci(1), 1)        
    
    def test_if_less_than_one(self):
        self.assertFalse(Fibonacci().fibonacci(0), False)        
    
    def test_if_many(self):
        self.assertEqual(Fibonacci().fibonacci(3), 2)  

if __name__ == '__main__':
    unittest.main()

    