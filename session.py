##
# @file session.py
# @brief Gère une session complète de Planning Poker.

from user import User
from story import Story
from vote import Vote

class Session:
    ##
    # @brief Constructeur de la session Planning Poker.
    # @param session_id Identifiant unique de la session.
    def _init_(self, session_id):
        self.session_id = session_id
        self.players = []
        self.scrum_master = None
        self.stories = []
        self.current_story = None

    ##
    # @brief Ajoute un joueur à la session.
    # @param user Joueur à ajouter.
    def add_player(self, user):
        if user.role == "SCRUM_MASTER":
            self.scrum_master = user
        else:
            self.players.append(user)

    ##
    # @brief Ajoute une User Story à estimer.
    # @param story Story à ajouter.
    def add_story(self, story):
        self.stories.append(story)

    ##
    # @brief Démarre la phase de vote pour une Story donnée.
    # @param story La story sélectionnée.
    def start_voting(self, story):
        self.current_story = story

    ##
    # @brief Termine la session de vote et calcule une estimation finale.
    # @return Estimation finale calculée.
    def end_voting(self):
        if self.current_story:
            return self.current_story.calculate_estimation()
