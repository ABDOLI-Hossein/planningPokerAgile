import json
import firebase_admin
from firebase_admin import credentials, firestore
from datetime import datetime

class Story:
    def __init__(self, description):
        self.description = description
        self.estimation = None

class Session:
    def __init__(self):
        self.backlog = []
        self.current_story = None
        self.users = []
        self.votes = {} 
        self.db = None
        
        # Connexion automatique au démarrage
        self.connect_firebase()

    def connect_firebase(self):
        """Initialise la connexion à Firestore."""
        try:
            # On vérifie si l'app n'est pas déjà initialisée pour éviter les erreurs
            if not firebase_admin._apps:
                # IMPORTANT : Assurez-vous que le nom du fichier est correct !
                cred = credentials.Certificate("serviceAccountKey.json")
                firebase_admin.initialize_app(cred)
            
            self.db = firestore.client()
            print("✅ SUCCÈS : Connecté à Firebase Firestore !")
        except Exception as e:
            print(f"❌ ERREUR Firebase : {e}")
            print("⚠️ L'application fonctionnera en mode local (sans sauvegarde).")
            self.db = None

    def ajouter_story_manuelle(self, description):
        nouvelle_story = Story(description)
        self.backlog.append(nouvelle_story)
        if self.current_story is None:
            self.current_story = nouvelle_story

    def register_user(self, user_obj):
        """Ajoute un utilisateur à la liste locale ET dans Firebase."""
        self.users.append(user_obj)
        
        # Sauvegarde dans Firebase
        if self.db:
            try:
                # On crée un document avec le nom du joueur
                self.db.collection("users").document(user_obj.name).set({
                    "name": user_obj.name,
                    "role": "Manager" if user_obj.is_manager else "Equipe",
                    "joined_at": datetime.now()
                })
                print(f"Firebase : Utilisateur {user_obj.name} sauvegardé.")
            except Exception as e:
                print(f"Erreur sauvegarde user : {e}")

    def add_vote(self, player_name, value):
        self.votes[player_name] = value
        print(f"Vote enregistré localement pour {player_name} : {value}")

    def validate_round(self):
        if self.current_story is None:
            return False, "Aucune story en cours."

        if not self.votes:
            return False, "Aucun vote n'a été enregistré."

        valeurs = list(self.votes.values())

        if "?" in valeurs:
            return False, "Débat nécessaire : Un participant a voté '?'"

        try:
            int_valeurs = [int(v) for v in valeurs]
        except ValueError:
            return False, "Erreur de valeur dans les cartes."

        # LOGIQUE DE VALIDATION
        if len(set(int_valeurs)) == 1:
            estimation_finale = int_valeurs[0]
            self.current_story.estimation = estimation_finale
            
            # --- SAUVEGARDE FIREBASE ---
            if self.db:
                doc_data = {
                    "story": self.current_story.description,
                    "estimation_finale": estimation_finale,
                    "details_votes": self.votes,  # Qui a voté quoi
                    "date": datetime.now(),
                    "participants": [u.name for u in self.users]
                }
                self.db.collection("historique_votes").add(doc_data)
                print("✅ Firebase : Résultat du vote sauvegardé dans 'historique_votes'.")
            # ---------------------------

            self.votes = {}
            self._passer_story_suivante()
            return True, f"Validé ! Estimation : {estimation_finale}"
        
        else:
            return False, f"Désaccord ! (Min: {min(int_valeurs)}, Max: {max(int_valeurs)})"

    def reset_votes_for_retry(self):
        self.votes = {}

    def load_data(self, filepath):
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                data = json.load(f)
                for item in data:
                    if isinstance(item, str):
                        self.backlog.append(Story(item))
                    elif isinstance(item, dict) and "description" in item:
                        self.backlog.append(Story(item["description"]))
            if self.backlog and self.current_story is None:
                self.current_story = self.backlog[0]
        except Exception as e:
            print(f"Erreur JSON: {e}")

    def _passer_story_suivante(self):
        try:
            idx = self.backlog.index(self.current_story)
            if idx + 1 < len(self.backlog):
                self.current_story = self.backlog[idx + 1]
            else:
                self.current_story = None
        except ValueError:
            self.current_story = None