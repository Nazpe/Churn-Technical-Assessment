import joblib
import os

# Load the model
model_path = os.path.join(os.path.dirname(__file__), 'model.pkl')
model = joblib.load(model_path)

def predict(input_data):
    return model.predict(input_data)