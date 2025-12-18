class Story:
    def __init__(self, title: str, description: str = "", id: str = "0"):
        self.id = id
        self.title = title
        self.description = description
        self.estimation = None 
    def set_estimation(self, value):
        self.estimation = value