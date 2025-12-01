"""
@file user.py
@author ...
@brief Defines the User class for Planning Poker.
"""

class User:
    """
    @class User
    @brief Represents a participant in the Planning Poker session.
    """

    def __init__(self, name: str):
        """
        @brief Constructor.
        @param name Name of the user.
        """
        self.name = name

    def get_name(self) -> str:
        """
        @brief Returns the user's name.
        @return string
        """
        return self.name
