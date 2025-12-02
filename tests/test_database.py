from database.mongo_manager import MongoManager


def test_db_connection():
    db = MongoManager()
    assert db.collection is not None
