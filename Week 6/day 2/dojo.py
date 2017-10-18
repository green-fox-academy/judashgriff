class Poker:
    def __init__(self):
        hands = [['D2', 'C3', 'H5', 'ST', 'DA'], ['D7', 'S3', 'H4', 'DT', 'DA']]
        self.card_values = {"2": 2,
                            "3": 3,
                            "4": 4,
                            "5": 5,
                            "6": 6,
                            "7": 7,
                            "8": 8,
                            "9": 9,
                            "T": 10,
                            "J": 11,
                            "Q": 12,
                            "K": 13,
                            "A": 14}
        self.cards_parser(hands)
        self.sorting_values()
        print(self.high_card(self.cards_parser(hands)))


    def cards_parser(self, hands):
        hand_one = [{}, {}, {}, {}, {}]
        hand_two = [{}, {}, {}, {}, {}] 
        self.first = self.parsing_hands(hand_one, 0)
        self.second = self.parsing_hands(hand_two, 1)

    def parsing_hands(self, hand, x):
        for num, i in enumerate(hand[x]):
            hand[num][list(i)[0]] = self.card_values[list(i)[1]]
        return hand
      
    def hands_dealt(self, hands):
        if hands == []:
            return 'No hands dealt.' 

    def high_card(self, hands):
        for num, i in enumerate(self.first_list):
            if self.first_list[num] > self.second_list[num] or self.first_list[num] < self.second_list[num]:
                if self.first_list[num] > self.second_list[num]:
                    return 'First hand wins, with high card'
                elif self.first_list[num] < self.second_list[num]:
                    return 'Second hand wins, with high card'

    # def find_higher(self, player_hand):
    #     highest = 0
    #     for i in player_hand:
    #         for key, val in i.items():
    #             if val > highest:
    #                 highest = val
    #     return highest

    def sorting_values(self):
        first_list = []
        second_list = []
        for i in self.first:
            for key, val in i.items():
                first_list.append(val)
        for i in self.second:
            for key, val in i.items():
                second_list.append(val)
        self.first_list = sorted(first_list, key=int, reverse=True)
        self.second_list = sorted(second_list, key=int, reverse=True)





game = Poker()