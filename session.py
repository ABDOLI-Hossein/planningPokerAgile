"""
@file session.py
@brief Defines a planning poker session.
"""

from user import User
from vote import Vote
from card import Card
from story import Story
from deck import Deck

class Session:
    """
    @class Session
    @brief Represents a planning poker session.
    """

    def __init__(self, story: Story):
        """
        @param story Story being estimated.
        """
        self.story = story
        self.users = []
        self.votes = []
        self.deck = Deck()

    def add_user(self, name: str):
        """
        @brief Add a new user.
        @param name User name
        """
        self.users.append(User(name))

    def add_vote(self, user_name: str, card_value: str):
        """
        @brief A user votes using a card.
        """
        user = next((u for u in self.users if u.get_name() == user_name), None)
        card = next((c for c in self.deck.get_cards() if c.get_value() == card_value), None)

        if user and card:
            self.votes.append(Vote(user, card))

    def get_votes(self):
        """
        @return list of Vote
        """
        return self.votes

    def show_results(self):
        """
        @brief Print vote results.
        """
        print(f"Estimation results for story: {self.story.get_title()}")
        for vote in self.votes:
            print(f"{vote.get_user().get_name()} voted {vote.get_card().get_value()}")
