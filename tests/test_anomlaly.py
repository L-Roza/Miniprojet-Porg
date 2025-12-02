from analytics.anomaly_detector import AnomalyDetector

def test_anomaly():
    detector = AnomalyDetector(100)
    assert detector.is_anomalous(120) == True
    assert detector.is_anomalous(80) == False
