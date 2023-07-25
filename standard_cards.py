class Card:
    card_type, card_name = "", ""
    card_value = 0

    def __init__(self, card_type, card_name, card_value):
        self.card_type = card_type
        self.card_name = card_name
        self.card_value = card_value

    def __str__(self):
        return f"{self.card_name} of {self.card_type}"


STARTING_DECK_31 = [
    Card("diamonds", "two", 2),
    Card("diamonds", "three", 3),
    Card("diamonds", "four", 4),
    Card("diamonds", "five", 5),
    Card("diamonds", "six", 6),
    Card("diamonds", "seven", 7),
    Card("diamonds", "eight", 8),
    Card("diamonds", "nine", 9),
    Card("diamonds", "ten", 10),
    Card("diamonds", "jack", 10),
    Card("diamonds", "queen", 10),
    Card("diamonds", "king", 10),
    Card("diamonds", "ace", 11),
    Card("hearts", "two", 2),
    Card("hearts", "three", 3),
    Card("hearts", "four", 4),
    Card("hearts", "five", 5),
    Card("hearts", "six", 6),
    Card("hearts", "seven", 7),
    Card("hearts", "eight", 8),
    Card("hearts", "nine", 9),
    Card("hearts", "ten", 10),
    Card("hearts", "jack", 10),
    Card("hearts", "queen", 10),
    Card("hearts", "king", 10),
    Card("hearts", "ace", 11),
    Card("spades", "two", 2),
    Card("spades", "three", 3),
    Card("spades", "four", 4),
    Card("spades", "five", 5),
    Card("spades", "six", 6),
    Card("spades", "seven", 7),
    Card("spades", "eight", 8),
    Card("spades", "nine", 9),
    Card("spades", "ten", 10),
    Card("spades", "jack", 10),
    Card("spades", "queen", 10),
    Card("spades", "king", 10),
    Card("spades", "ace", 11),
    Card("clubs", "two", 2),
    Card("clubs", "three", 3),
    Card("clubs", "four", 4),
    Card("clubs", "five", 5),
    Card("clubs", "six", 6),
    Card("clubs", "seven", 7),
    Card("clubs", "eight", 8),
    Card("clubs", "nine", 9),
    Card("clubs", "ten", 10),
    Card("clubs", "jack", 10),
    Card("clubs", "queen", 10),
    Card("clubs", "king", 10),
    Card("clubs", "ace", 11)
]


def get_deck_copy():
    return STARTING_DECK_31.copy()




