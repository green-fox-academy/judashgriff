# Potter

# Once upon a time there was a series of 5 books about a very English hero called Harry. 
# (At least when this Kata was invented, there were only 5. Since then they have multiplied) 
# Children all over the world thought he was fantastic, and, of course, so did the publisher.
#  So in a gesture of immense generosity to mankind, 
# (and to increase sales) they set up the following pricing model to take advantage of Harry's magical powers.

# One copy of any of the five books costs 8 EUR. If, however, you buy two different books from 
# the series, you get a 5% discount on those two books. If you buy 3 different books, you get a 
# 10% discount. With 4 different books, you get a 20% discount. If you go the whole hog, and buy 
# all 5, you get a huge 25% discount.

# Note that if you buy, say, four books, of which 3 are different titles, you get a 10% discount
#  on the 3 that form part of a set, but the fourth book still costs 8 EUR.

# Potter mania is sweeping the country and parents of teenagers everywhere are queueing up with 
# shopping baskets overflowing with Potter books. Your mission is to write a piece of code to 
# calculate the price of any conceivable shopping basket, giving as big a discount as possible.

# For example, how much does this basket of books cost?

# 2 copies of the first book
# 2 copies of the second book
# 2 copies of the third book
# 1 copy of the fourth book
# 1 copy of the fifth book (answer: 51.20 EUR)
# Clues

# You’ll find that this Kata is easy at the start. You can get going with tests for baskets 
# of 0 books, 1 book, 2 identical books, 2 different books… and it is not too difficult to work
#  in small steps and gradually introduce complexity.

# However, the twist becomes apparent when you sit down and work out how much you think the sample
#  basket above should cost. It isn’t 580.75+380.90. It is in fact 480.8+480.8. So the trick with
#   this Kata is not that the acceptance test you’ve been given is wrong. The trick is that you
#    have to write some code that is intelligent enough to notice that two sets of four books is
#     cheaper than a set of five and a set of three.

# You will have to introduce a certain amount of clever optimization algorithm. But not too much! 
# This problem does not require a fully fledged general purpose optimizer. Try to solve just this 
# problem well in order to share it for everyone or even in the ??? . Trust that you can generalize
#  and improve your solution if and when new requirements come along.

import unittest
import harry


class TestHarry(unittest.TestCase):

    def test_empty_bucket(self):
        self.assertEqual(harry.books_cost([]), 0)
    
    def test_one_book(self):
        self.assertEqual(harry.books_cost(["1"]), 8)

    def test_two_of_the_same(self):
        self.assertEqual(harry.books_cost(["1", "1"]), 16)

    def test_two_of_two_kinds(self):
        self.assertEqual(harry.books_cost(["1", "2"]), 16*0.95)

    def test_many_of_the_same(self):
        self.assertEqual(harry.books_cost(["1", "1", "1"]), 24)

    def test_two_same_and_one_different(self):
        self.assertEqual(harry.books_cost(["1", "1", "2"]), 16*0.95+8)

if __name__ == "__main__":
    unittest.main()