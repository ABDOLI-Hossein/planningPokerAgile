"""
@file story.py
@brief Defines a story/feature to estimate.
"""

class Story:
    """
    @class Story
    @brief A task or feature to estimate.
    """

    def __init__(self, title: str, description: str = ""):
        """
        @param title Story title
        @param description Story description
        """
        self.title = title
        self.description = description

    def get_title(self):
        """
        @return Story title
        """
        return self.title

    def get_description(self):
        """
        @return Story description
        """
        return self.description
