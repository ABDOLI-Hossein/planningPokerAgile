"""
@file vote.py
@brief Defines the Vote class.
"""

from user import User
from card import Card

class Vote:
    """
    @class Vote
    @brief Represents a vote made by a user.
    """

    def __init__(self, user: User, card: Card):
        """
        @param user The voting user
        @param card The chosen card
        """
        self.user = user
        self.card = card

    def get_user(self):
        """
        @return User object
        """
        return self.user

    def get_card(self):
        """
        @return Card object
        """
        return self.card
