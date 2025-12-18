import pytest
import sys
import os

# Ajoute le dossier parent au path pour importer les modules
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from rules import Rules
from card import Card
from vote import Vote
from user import User

class TestRules:
    
    def test_strict_unanimous(self):
        """Vérifie que l'unanimité fonctionne."""
        u1 = User("Alice")
        u2 = User("Bob")
        c1 = Card("5")
        
        votes = [Vote(u1, c1), Vote(u2, c1)]
        assert Rules.is_unanimous(votes) == True

    def test_strict_fail(self):
        """Vérifie que le désaccord est détecté."""
        u1 = User("Alice")
        u2 = User("Bob")
        v1 = Vote(u1, Card("5"))
        v2 = Vote(u2, Card("8"))
        
        votes = [v1, v2]
        success, result = Rules.calculate_result(votes, mode="strict")
        assert success == False

    def test_average(self):
        """Vérifie le calcul de la moyenne."""
        u1 = User("Alice")
        u2 = User("Bob")
        # Moyenne de 5 et 8 = 6.5 -> arrondi ou traité selon votre logique
        # Ici selon le code donné : (5+8)/2 = 6.5
        votes = [Vote(u1, Card("5")), Vote(u2, Card("8"))]
        
        success, result = Rules.calculate_result(votes, mode="moyenne")
        assert success == True
        assert result == "6.5"  # Car rules.py retourne un str(round(avg, 1))

    def test_coffee_break(self):
        """Vérifie la règle spéciale Café."""
        votes = [Vote(User("A"), Card("?")), Vote(User("B"), Card("?"))]
        success, result = Rules.calculate_result(votes)
        assert result == "COFFEE_BREAK"

if __name__ == "__main__":
    pytest.main()