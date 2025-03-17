# predict.py
from flask import Flask, request, jsonify
import torch
import pandas as pd
from model import load_model

# Device Configuration
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

# Load cols_to_drop dynamically
def load_cols_to_drop():
    with open("cols_to_drop.txt", "r") as file:
        return [col.strip().strip("'").strip('"') for col in file.read().strip().split(",")]


# Dynamically Calculate Input Dimension
def get_input_dim():
    cols_to_drop = load_cols_to_drop()
    return 448 - len(cols_to_drop) + 3


# Load Model
model = load_model(input_dim=get_input_dim()).to(device)

# Flask App
app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    cols_to_drop = load_cols_to_drop()

    df = pd.DataFrame([data['input']])

    # Calculate NDVI, NDWI, SAVI
    red_band, nir_band, swir_band = '40', '100', '200'
    L = 0.5
    df['NDVI'] = (df[nir_band] - df[red_band]) / (df[nir_band] + df[red_band])
    df['NDWI'] = (df[nir_band] - df[swir_band]) / (df[nir_band] + df[swir_band])
    df['SAVI'] = (df[nir_band] - df[red_band]) / (df[nir_band] + df[red_band] + L) * (1 + L)

    # Drop unnecessary columns
    df = df.drop(columns=cols_to_drop, axis=1)

    # Convert to Torch Tensor
    input_tensor = torch.tensor(df.values).float().to(device)

    # Model Prediction
    with torch.no_grad():
        prediction = model(input_tensor).cpu().numpy()

    return jsonify({'predictions': prediction.tolist()})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)