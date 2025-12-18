from card import Card
class Deck:
    def __init__(self):
        values = ["1", "2", "3", "5", "8", "13", "21", "?"]
        self.cards = [Card(v) for v in values]
    def get_cards(self):
        return self.cards