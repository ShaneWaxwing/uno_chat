class player:

    def __init__(self, name, wins, losses):
        self.name = name
        self.wins = wins
        self.losses = losses


class Card:
    def __init__(self, color, number):
        self.color = color
        self.number = number



class Deck:
    def __init__(self, card):
        self.card = card