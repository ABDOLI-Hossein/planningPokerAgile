##
# @file session.py
# @brief Gère une session complète de Planning Poker (joueurs, stories, votes).
# @version 1.0

from user import User
from story import Story
from vote import Vote

class Session:
    ##
    # @brief Constructeur de la session Planning Poker.
    # @param session_id Identifiant unique de la session.
    def __init__(self, session_id):
        self.session_id = session_id
        self.players = []       # liste d'objets User (players)
        self.scrum_master = None
        self.stories = []       # liste d'objets Story
        self.current_story = None

    ##
    # @brief Ajoute un joueur à la session.
    # @param user Instance de User.
    def add_player(self, user):
        if not isinstance(user, User):
            raise TypeError("add_player attend un User")
        if user.get_role() == "SCRUM_MASTER":
            self.scrum_master = user
        else:
            # éviter les doublons
            if all(p.get_id() != user.get_id() for p in self.players):
                self.players.append(user)

    ##
    # @brief Ajoute une User Story à la session.
    # @param story Instance de Story.
    def add_story(self, story):
        if not isinstance(story, Story):
            raise TypeError("add_story attend un Story")
        self.stories.append(story)

    ##
    # @brief Sélectionne une story pour démarrer le vote.
    # @param story Instance de Story.
    def start_voting(self, story):
        if story not in self.stories:
            raise ValueError("La story doit être ajoutée à la session avant de lancer le vote")
        self.current_story = story

    ##
    # @brief Ajoute un vote à la story courante.
    # @param vote Instance de Vote.
    def cast_vote(self, vote):
        if self.current_story is None:
            raise RuntimeError("Aucune story en cours de vote")
        self.current_story.add_vote(vote)

    ##
    # @brief Termine le vote pour la story courante et calcule l'estimation finale.
    # @return estimation finale calculée.
    def end_voting(self):
        if self.current_story is None:
            return None
        estimation = self.current_story.calculate_estimation()
        self.current_story = None
        return estimation

    ##
    # @brief Représentation textuelle de la session.
    # @return Chaîne descriptive.
    def __str__(self):
        return f"Session(id={self.session_id}, players={len(self.players)}, stories={len(self.stories)})"
