"""
@file deck.py
@brief Defines the deck of Planning Poker cards.
"""

from card import Card

class Deck:
    """
    @class Deck
    @brief The complete set of Planning Poker cards.
    """

    def __init__(self):
        """
        @brief Initializes all possible Planning Poker cards.
        """
        values = ["1", "2", "3", "5", "8", "13", "21", "?"]
        self.cards = [Card(v) for v in values]

    def get_cards(self):
        """
        @brief Returns all cards.
        @return list of Card
        """
        return self.cards
