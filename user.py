##
# @file user.py
# @brief Définit la classe User représentant un joueur dans une session de Planning Poker.
# @author ...
# @version 1.0

class User:
    ##
    # @brief Constructeur de la classe User.
    # @param user_id Identifiant unique du joueur.
    # @param name Nom du joueur.
    # @param role Rôle du joueur (PLAYER ou SCRUM_MASTER).
    def _init_(self, user_id, name, role="PLAYER"):
        self.user_id = user_id
        self.name = name
        self.role = role

    ##
    # @brief Retourne le nom du joueur.
    # @return Le nom du joueur.
    def get_name(self):
        return self.name
