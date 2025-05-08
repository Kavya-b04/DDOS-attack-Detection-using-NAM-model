from flask import Flask, render_template, request, jsonify
import torch
import torch.nn as nn
import numpy as np
import joblib

app = Flask(__name__)  # Corrected __name__

# === NAM Model Definition ===
class NAM(nn.Module):
    def __init__(self, input_dim=5, hidden_dim=128, num_classes=2):
        super(NAM, self).__init__()
        self.nam_layers = nn.ModuleList([
            nn.Sequential(
                nn.Linear(1, hidden_dim),
                nn.ReLU(),
                nn.Linear(hidden_dim, 1)
            ) for _ in range(input_dim)
        ])
        self.output = nn.Linear(input_dim, num_classes)

    def forward(self, x):
        outputs = [layer(x[:, i:i+1]) for i, layer in enumerate(self.nam_layers)]
        combined = torch.cat(outputs, dim=1)
        return self.output(combined)

# === Load Model & Scaler ===
model = NAM()
model.load_state_dict(torch.load('best_nam_model.pth', map_location=torch.device('cpu')))
model.eval()

scaler = joblib.load('nam_scaler.save')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        features = data.get('features')

        # Scale input
        scaled = scaler.transform([features])
        input_tensor = torch.tensor(scaled, dtype=torch.float32)

        # Model prediction
        with torch.no_grad():
            outputs = model(input_tensor)
            probs = torch.softmax(outputs, dim=1).numpy().flatten()
            _, predicted = torch.max(outputs, 1)

        result_text = 'DDoS Attack Detected!' if predicted.item() == 1 else 'Normal Traffic'
        contributions = np.abs(scaled.flatten()).tolist()

        return jsonify({
            'prediction': predicted.item(),
            'result_text': result_text,
            'probs': probs.tolist(),
            'contributions': contributions,
            'features_used': features  # Send back original features for graph
        })

    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
