class User:
    def __init__(self, name: str, is_manager: bool = False):
        self.name = name
        self.is_manager = is_manager # True = Manager, False = Voteur

    def get_name(self) -> str:
        return self.name
        
    def get_role_name(self) -> str:
        return "Manager" if self.is_manager else "Équipe"