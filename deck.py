##
# @file deck.py
# @brief Gère le paquet de cartes utilisées pour voter.

from card import Card

class Deck:
    ##
    # @brief Constructeur du paquet de cartes.
    def _init_(self):
        self.cards = []

    ##
    # @brief Crée un paquet standard Fibonacci.
    # @return Un objet Deck contenant les cartes standards.
    @staticmethod
    def default_deck():
        deck = Deck()
        values = [1, 2, 3, 5, 8, 13, 21, "?" , "☕"]
        deck.cards = [Card(v) for v in values]
        return deck
