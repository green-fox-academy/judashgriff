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
print(numbers.sum_of_list(list_of_nums))