from capteurs.capteur import Capteur
from database.mongo_manager import MongoManager
from analytics.anomaly_detector import AnomalyDetector
import time


def main():
    capteur = Capteur("Salle_serveurs", 0, 300)
    db = MongoManager()
    detector = AnomalyDetector(threshold=250)

    for _ in range(20):
        measurement = capteur.read_value()
        db.insert_measurement(measurement)
        # print("📌 Mesure enregistrée dans MongoDB :",measurement )
        if detector.is_anomalous(measurement["valeurs"]):
            print(f"⚠ Anomalie détectée ! Valeur = {measurement['valeurs']}")

        time.sleep(1)


if __name__ == "__main__":
    main()
