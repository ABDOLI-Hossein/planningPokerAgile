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
    # @param role Rôle du joueur (ex: "PLAYER" ou "SCRUM_MASTER").
    def __init__(self, user_id, name, role="PLAYER"):
        self.user_id = user_id
        self.name = name
        self.role = role

    ##
    # @brief Retourne l'identifiant du joueur.
    # @return Identifiant utilisateur.
    def get_id(self):
        return self.user_id

    ##
    # @brief Retourne le nom du joueur.
    # @return Nom du joueur.
    def get_name(self):
        return self.name

    ##
    # @brief Retourne le rôle du joueur.
    # @return Rôle (PLAYER ou SCRUM_MASTER).
    def get_role(self):
        return self.role

    ##
    # @brief Représentation textuelle.
    # @return Chaîne représentant l'utilisateur.
    def __str__(self):
        return f"User(id={self.user_id}, name='{self.name}', role='{self.role}')"
