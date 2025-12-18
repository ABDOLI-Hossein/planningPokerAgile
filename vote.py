from user import User
from card import Card
class Vote:
    def __init__(self, user: User, card: Card):
        self.user = user
        self.card = card
    def get_user(self): return self.user
    def get_card(self): return self.card