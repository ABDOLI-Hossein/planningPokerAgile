##
# @file vote.py
# @brief Contient la classe Vote, représentant le vote d'un joueur.

class Vote:
    ##
    # @brief Constructeur d'un vote.
    # @param user Joueur qui vote.
    # @param card Carte choisie par le joueur.
    def _init_(self, user, card):
        self.user = user
        self.card = card
