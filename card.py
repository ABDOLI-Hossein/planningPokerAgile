##
# @file card.py
# @brief Définition d'une carte représentant une estimation dans Planning Poker.

class Card:
    ##
    # @brief Constructeur d'une carte.
    # @param value Valeur numérique ou symbole de la carte (ex: 1, 2, 3, 5, 8, ?, ☕).
    def _init_(self, value):
        self.value = value
