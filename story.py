##
# @file story.py
# @brief Représente une User Story à estimer dans une session Planning Poker.
# @version 1.0

from vote import Vote

class Story:
    ##
    # @brief Constructeur de la User Story.
    # @param story_id Identifiant de la story.
    # @param title Titre court de la story.
    # @param description Description détaillée (optionnelle).
    def __init__(self, story_id, title, description=""):
        self.story_id = story_id
        self.title = title
        self.description = description
        self.votes = []  # List[Vote]
        self.final_estimation = None

    ##
    # @brief Ajoute un vote à cette User Story.
    # @param vote Objet Vote à ajouter.
    def add_vote(self, vote):
        if not isinstance(vote, Vote):
            raise TypeError("add_vote attend un objet Vote")
        # remplacer vote si l'utilisateur a déjà voté
        for i, v in enumerate(self.votes):
            if v.get_user().get_id() == vote.get_user().get_id():
                self.votes[i] = vote
                return
        self.votes.append(vote)

    ##
    # @brief Retourne la liste des votes.
    # @return liste d'objets Vote.
    def get_votes(self):
        return self.votes

    ##
    # @brief Calcule l'estimation finale par moyenne des votes numériques.
    # @return estimation calculée (float) ou "Indeterminée" si aucun vote numérique.
    def calculate_estimation(self):
        numeric_votes = []
        for v in self.votes:
            val = v.get_card().get_value()
            if isinstance(val, (int, float)):
                numeric_votes.append(val)
        if len(numeric_votes) == 0:
            self.final_estimation = "Indeterminée"
        else:
            self.final_estimation = sum(numeric_votes) / len(numeric_votes)
        return self.final_estimation

    ##
    # @brief Représentation textuelle de la story.
    # @return Chaîne descriptive.
    def __str__(self):
        return f"Story(id={self.story_id}, title='{self.title}')"
