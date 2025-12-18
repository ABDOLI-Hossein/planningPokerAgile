"""
@file firebase_db.py
@brief Gestion de la connexion Firebase Realtime Database.
"""
import firebase_admin
from firebase_admin import credentials, db
import os

class FirebaseManager:
    _instance = None

    def __init__(self):
        if not firebase_admin._apps:
            cred_path = "serviceAccountKey.json"
            if os.path.exists(cred_path):
                cred = credentials.Certificate(cred_path)
                # L'URL de votre DB se trouve dans la console Firebase
                # Remplacez l'URL ci-dessous par la vôtre si nécessaire, 
                # sinon firebase-admin la trouve souvent via le JSON.
                try:
                    firebase_admin.initialize_app(cred, {
                        'databaseURL': 'https://YOUR_PROJECT_ID.firebaseio.com/' 
                        # Note: Remplacez YOUR_PROJECT_ID par l'ID de votre projet 
                        # ou laissez vide si le JSON contient l'info correcte.
                    })
                    print("Firebase connecté !")
                except ValueError:
                    # Déjà initialisé
                    pass
            else:
                print("Erreur: serviceAccountKey.json manquant.")

    @staticmethod
    def save_vote(story_id, user, value):
        try:
            ref = db.reference(f'votes/{story_id}')
            ref.child(user).set(value)
        except Exception as e:
            print(f"Erreur Firebase (Save Vote): {e}")

    @staticmethod
    def get_backlog():
        """Récupère le backlog depuis Firebase ou renvoie None."""
        try:
            ref = db.reference('backlog')
            return ref.get()
        except Exception:
            return None

    @staticmethod
    def upload_backlog(json_data):
        """Pour initialiser Firebase avec votre JSON local."""
        try:
            ref = db.reference('backlog')
            ref.set(json_data)
        except Exception as e:
            print(f"Erreur Upload: {e}")