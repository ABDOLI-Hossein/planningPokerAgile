##
# @file card.py
# @brief Définition d'une carte représentant une estimation dans Planning Poker.
# @version 1.0

class Card:
    ##
    # @brief Constructeur d'une carte.
    # @param value Valeur numérique ou symbole de la carte (ex: 1, 2, 3, 5, 8, "?", "☕").
    def __init__(self, value):
        self.value = value

    ##
    # @brief Retourne la valeur de la carte.
    # @return Valeur (int ou str).
    def get_value(self):
        return self.value

    ##
    # @brief Représentation textuelle.
    # @return Chaîne représentant la carte.
    def __str__(self):
        return f"Card({self.value})"
