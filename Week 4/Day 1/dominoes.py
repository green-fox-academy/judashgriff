class Domino(object):
    def __init__(self, value_a, value_b):
        self.values = [value_a, value_b]

    def __repr__(self):
        return '[{}, {}]'.format(self.values[0], self.values[1])


def initialize_dominoes():
    dominoes = []
    dominoes.append(Domino(5, 2))
    dominoes.append(Domino(4, 6))
    dominoes.append(Domino(1, 5))
    dominoes.append(Domino(6, 7))
    dominoes.append(Domino(2 ,4))
    dominoes.append(Domino(7, 1))
    return dominoes


dominoes = initialize_dominoes()

def domino_sorter(the_object):
    correct_order = []
    correct_order.append(the_object[0])
    for i in range(len(the_object)):
        for j in range(len(the_object)):
            if correct_order[-1].values[1] == the_object[j].values[0] and len(correct_order) < len(the_object):
                correct_order.append(the_object[j]) 
    print(correct_order)

domino_sorter(dominoes)

# print(type(dominoes[0]))

# You have the list of Dominoes
# Order them into one snake where the adjacent dominoes have the same numbers on their adjacent sides
# eg: [2, 4], [4, 3], [3, 5] ...




