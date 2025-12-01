##
# @file main.py
# @brief Point d'entrée de démonstration du projet Planning Poker.
# @version 1.0

from user import User
from story import Story
from card import Card
from vote import Vote
from session import Session
from deck import Deck

def demo():
    # Création de la session
    session = Session("S001")

    # Utilisateurs
    u1 = User(1, "Alice")
    u2 = User(2, "Bob")
    sm = User(99, "Eve", "SCRUM_MASTER")

    session.add_player(u1)
    session.add_player(u2)
    session.add_player(sm)

    # Deck par défaut (non utilisé directement ici mais disponible)
    deck = Deck.default_deck()
    print(deck)

    # Création d'une story
    story = Story(10, "Créer API login", "Permettre l'authentification des utilisateurs")
    session.add_story(story)

    # Lancer le vote pour la story
    session.start_voting(story)

    # Les joueurs votent (exemple)
    session.cast_vote(Vote(u1, Card(5)))
    session.cast_vote(Vote(u2, Card(8)))

    # Fin du vote et estimation
    estimation = session.end_voting()
    print("Estimation finale pour la story:", estimation)

if __name__ == "__main__":
    demo()
