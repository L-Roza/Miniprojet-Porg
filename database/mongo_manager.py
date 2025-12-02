'''On va enregistrer les mesures des capteurs dans une base de données MongoDB.'''
from pymongo import MongoClient


class MongoManager:
    def __init__(self, uri="mongodb://localhost:27017",  db_name="EnergyDB"):
        self.client = MongoClient(uri)
        self.db = self.client[db_name]
        self.collection = self.db["mesures"]

    def insert_measurement(self, data):
        self.collection.insert_one(data)

    def get_all_measurements(self):
        return list(self.collection.find())
