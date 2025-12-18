import json
from story import Story
from firebase_db import FirebaseManager

class Persistence:
    @staticmethod
    def load_backlog(filename: str):
        stories = []
        # Essayer d'abord Firebase
        fb_data = FirebaseManager.get_backlog()
        
        data_source = fb_data if fb_data else []
        
        # Si Firebase vide, repli sur fichier local
        if not data_source:
            try:
                with open(filename, 'r', encoding='utf-8') as f:
                    data_source = json.load(f)
                    # On en profite pour upload sur Firebase pour la prochaine fois
                    FirebaseManager.upload_backlog(data_source)
            except FileNotFoundError:
                return []

        # Conversion en objets Story
        if isinstance(data_source, list):
            for item in data_source:
                if item and "estimation" not in item:
                    stories.append(Story(item["title"], item.get("description", ""), item.get("id", "0")))
        return stories

    @staticmethod
    def save_state(filename, done, remaining):
        data = []
        for s in done + remaining:
            data.append({"id": s.id, "title": s.title, "desc": s.description, "est": s.estimation})
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4)