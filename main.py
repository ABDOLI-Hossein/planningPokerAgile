"""
@file main.py
@brief Main entry point for the Planning Poker application.
"""

from session import Session
from story import Story

def main():
    """
    @brief Run a simple Planning Poker scenario.
    """
    story = Story("User Login Feature", "Implement login with email and password")
    session = Session(story)

    session.add_user("Alice")
    session.add_user("Bob")

    session.add_vote("Alice", "5")
    session.add_vote("Bob", "8")

    session.show_results()

if __name__ == "__main__":
    main()
