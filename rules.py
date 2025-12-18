import statistics

class Rules:
    @staticmethod
    def calculate_result(votes, mode="strict"):
        if not votes: return False, "Aucun vote"
        
        # Gestion Café
        coffee = [v for v in votes if v.get_card().get_value() == "?"]
        if len(coffee) == len(votes): return False, "COFFEE_BREAK"

        # Valeurs numériques
        nums = [int(v.get_card().get_value()) for v in votes if v.get_card().get_value().isdigit()]
        if not nums: return False, "Votes invalides"

        if mode == "strict":
            if all(x == nums[0] for x in nums): return True, str(nums[0])
            return False, "Pas d'unanimité"
        
        elif mode == "moyenne":
            return True, str(round(statistics.mean(nums), 1))
            
        return False, "Mode inconnu"