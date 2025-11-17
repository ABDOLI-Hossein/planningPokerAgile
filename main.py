##
# @file main.py
# @brief Point d'entrée du programme Planning Poker.

from user import User
from story import Story
from card import Card
from vote import Vote
from session import Session

##
# @brief Fonction principale de démonstration.
def main():

    session = Session("S001")

    # Création des utilisateurs
    u1 = User(1, "Alice")
    u2 = User(2, "Bob")
    sm = User(99, "ScrumMaster", "SCRUM_MASTER")

    session.add_player(u1)
    session.add_player(u2)
    session.add_player(sm)

    # User story
    story = Story(10, "Créer API login", "Permettre l'authentification")
    session.add_story(story)
    session.start_voting(story)

    # Votes
    story.add_vote(Vote(u1, Card(5)))
    story.add_vote(Vote(u2, Card(8)))

    estimation = session.end_voting()
    print("Estimation finale :", estimation)

if _name_ == "_main_":
    main()
## commentaire2
