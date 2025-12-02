from capteurs.capteur import Capteur


def test_capteur_read():
    s = Capteur("test", 0, 50)
    data = s.read_value()
    assert 0 <= data["valeurs"] <= 50
