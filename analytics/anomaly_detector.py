class AnomalyDetector:
    def __init__(self, threshold):
        self.threshold = threshold

    def is_anomalous(self, value):
        return value > self.threshold
