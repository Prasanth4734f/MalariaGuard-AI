import joblib


class PredictionEngine:

    LOW_THRESHOLD = 500
    HIGH_THRESHOLD = 1500

    def __init__(self, model_path):

        self.model_path = model_path
        self.model = None

    # ==========================================
    # Load Model
    # ==========================================

    def load_model(self):

        if self.model is not None:
            return

        print("Loading AI Model...")

        self.model = joblib.load(self.model_path)

        print("Random Forest Model Loaded Successfully")

    # ==========================================
    # Predict
    # ==========================================

    def predict(self, features):

        prediction = round(
            float(self.model.predict(features)[0]),
            2
        )

        return {
            "prediction": prediction,
            "risk": self.get_risk_level(prediction)
        }

    # ==========================================
    # Risk Level
    # ==========================================

    def get_risk_level(self, prediction):

        if prediction < self.LOW_THRESHOLD:
            return "🟢 LOW"

        elif prediction < self.HIGH_THRESHOLD:
            return "🟡 MODERATE"

        else:
            return "🔴 HIGH"