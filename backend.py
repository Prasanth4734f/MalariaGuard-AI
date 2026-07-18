from data_engine import DataEngine
from prediction import PredictionEngine

# Load everything only once
engine = DataEngine("Final_Data.csv")
engine.initialize()

predictor = PredictionEngine("rf_model.pkl")
predictor.load_model()


def predict_district(district):

    features = engine.prepare_features(district)

    if features is None:
        return None

    result = predictor.predict(features)

    details = engine.get_record(district)

    return {
        "district": district,
        "prediction": result["prediction"],
        "risk": result["risk"],
        "weather": {
            "temperature": details["T2M"],
            "humidity": details["RH2M"],
            "rainfall": details["PRECIP"]
        },
        "deaths": details["malaria_deaths"],
        "date": details["DATE"]
    }