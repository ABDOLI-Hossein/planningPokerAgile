##
# @file vote.py
# @brief Contient la classe Vote, représentant le vote d'un joueur pour une story.
# @version 1.0

class Vote:
    ##
    # @brief Constructeur d'un vote.
    # @param user Joueur qui vote (instance de User).
    # @param card Carte choisie par le joueur (instance de Card).
    def __init__(self, user, card):
        self.user = user
        self.card = card

    ##
    # @brief Retourne le joueur ayant voté.
    # @return Instance de User.
    def get_user(self):
        return self.user

    ##
    # @brief Retourne la carte choisie.
    # @return Instance de Card.
    def get_card(self):
        return self.card

    ##
    # @brief Représentation textuelle du vote.
    # @return Chaîne décrivant le vote.
    def __str__(self):
        return f"Vote(user={self.user.get_name()}, card={self.card.get_value()})"
