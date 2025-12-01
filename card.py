"""
@file card.py
@brief Defines the Card class.
"""

class Card:
    """
    @class Card
    @brief Planning Poker card (1,2,3,5,8,...,?)
    """

    def __init__(self, value: str):
        """
        @param value Card value
        """
        self.value = value

    def get_value(self) -> str:
        """
        @return the card value
        """
        return self.value
