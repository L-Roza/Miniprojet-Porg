import random
from datetime import datetime


class Capteur:
    def __init__(self, name, min_value=0, max_value=100):
        self.name = name
        self.min_value = min_value  # Valeur minimale qu’il peut mesurer
        self.max_value = max_value  # Valeur maximale qu’il peut mesurer

    def read_value(self):
        # la fonction renvoie un dictionnaire qui contient toutes les informations de la mesure
        return {
            "Capteur": self.name,
            "valeurs": random.uniform(self.min_value, self.max_value), "Horaires": datetime.now()
            # random.uniform Génère une valeur aléatoire réaliste
            # datetime.now() Ajoute la date et l’heure de la mesure
        }
