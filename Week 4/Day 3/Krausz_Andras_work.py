class Getting_apple(object):
    def get_apple(self):
        return "apple"


class Sum(object):
    def sum_of_list(self, list_of_nums):
        total = 0
        for i in list_of_nums:
            total += i
        return total

list_of_nums = [5, 4, 9]

numbers = Sum()
numbers.sum_of_list(list_of_nums)


class Anagram(object):
    def anagram(self, string):
        if string == string[::-1]:
            return True
        return False

string = Anagram()
string.anagram("indulagörögaludni")


class Count_letters(object):
    def count_letters(self, word):
        dict_of_chars = {}
        for letter in word:
            if letter in dict_of_chars:
                dict_of_chars[letter] += 1
            else:
                dict_of_chars[letter] = 1
        return dict_of_chars


class Fibonacci(object):
    def fibonacci(self, num):
        if num == 1:
            return num
        elif num < 1:
            return False
        else:
            return self.fibonacci(num-2) + self.fibonacci(num-1)

        