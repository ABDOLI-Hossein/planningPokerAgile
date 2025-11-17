##
# @file story.py
# @brief Représente une User Story à estimer dans une session Planning Poker.

from vote import Vote

class Story:
    ##
    # @brief Constructeur de la User Story.
    # @param story_id Identifiant de la story.
    # @param title Titre court de la story.
    # @param description Description de la story.
    def _init_(self, story_id, title, description=""):
        self.story_id = story_id
        self.title = title
        self.description = description
        self.votes = []
        self.final_estimation = None

    ##
    # @brief Ajoute un vote à cette User Story.
    # @param vote Objet Vote à ajouter.
    def add_vote(self, vote):
        self.votes.append(vote)

    ##
    # @brief Calcule l'estimation finale (simple moyenne).
    # @return L'estimation calculée.
    def calculate_estimation(self):
        numeric_votes = [v.card.value for v in self.votes if isinstance(v.card.value, int)]

        if len(numeric_votes) == 0:
            self.final_estimation = "Indeterminée"
        else:
            self.final_estimation = sum(numeric_votes) / len(numeric_votes)

        return self.final_estimation
