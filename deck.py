##
# @file deck.py
# @brief Gère le paquet de cartes utilisées pour voter dans Planning Poker.
# @version 1.0

from card import Card

class Deck:
    ##
    # @brief Constructeur du paquet de cartes.
    def __init__(self, cards=None):
        self.cards = cards if cards is not None else []

    ##
    # @brief Crée un paquet standard (Fibonacci-like) avec quelques symboles.
    # @return Un objet Deck contenant les cartes standards.
    @staticmethod
    def default_deck():
        default_values = [1, 2, 3, 5, 8, 13, 21, "?", "☕"]
        return Deck([Card(v) for v in default_values])

    ##
    # @brief Retourne la liste des cartes.
    # @return Liste d'objets Card.
    def get_cards(self):
        return self.cards

    ##
    # @brief Ajoute une carte au paquet.
    # @param card Objet Card à ajouter.
    def add_card(self, card):
        self.cards.append(card)

    ##
    # @brief Représentation textuelle du paquet.
    # @return Chaîne listant les cartes.
    def __str__(self):
        vals = ', '.join(str(c.get_value()) for c in self.cards)
        return f"Deck([{vals}])"
