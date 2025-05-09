# 🚨 AnomalyNet - DDoS Attack Detection using Neural Additive Models

AnomalyNet is a web-based AI-powered tool designed for detecting DDoS (Distributed Denial of Service) attacks in network traffic using a Neural Additive Model (NAM). It features a sleek interactive UI with live visualizations of feature contributions and traffic metrics.

---

## 📌 Features

- 🧠 **NAM Model**: Built using PyTorch, trained on labeled traffic flow data.
- ⚖️ **Explainability**: Visual feature contributions for interpretability.
- 🌐 **Web Interface**: Responsive UI built with HTML, JS (Chart.js), and Flask backend.
- 📊 **Live Graphs**: Real-time bar charts for feature impact and current traffic.
- 🌙 **Theme Toggle**: Switch between light and dark modes for better visibility.

---

## 🚀 Demo

![UI Preview](![WhatsApp Image 2025-05-07 at 20 58 58_3994553b](https://github.com/user-attachments/assets/55503528-32ab-4140-94b2-e8e0e94707b9)
![WhatsApp Image 2025-05-07 at 20 59 23_1a55118f](https://github.com/user-attachments/assets/3f5c4045-7e2e-4d03-81d8-3f27f5db74df)) <!-- Add your UI screenshot here -->

---

## 🏗️ Project Structure
├── app.py # Flask app and model API
├── best_nam_model.pth # Trained PyTorch NAM model
├── nam_scaler.save # Scaler used for preprocessing input features
├── templates/
│ └── index.html # Frontend UI
├── README.md


---

## 🔧 How It Works

1. **User Input**: Enter 5 selected traffic flow features.
2. **Preprocessing**: Features are scaled using a saved `StandardScaler`.
3. **Prediction**: NAM model outputs DDoS (1) or Normal (0).
4. **Explainability**: Each feature’s contribution is visualized.
5. **Live Monitoring**: Current input is charted as real-time traffic.

---

## 📥 Setup Instructions

### 1. Clone the Repository

git clone https://github.com/kavya-b04/DDOS-attack-Detection-using-NAM-model.git
cd ddos-nam-detector

2. Install Dependencies
bash
Copy code
pip install -r requirements.txt

3. Run the App
bash
Copy code
python app.py
Visit http://127.0.0.1:5000 in your browser.

📊 Input Features Used
Flow Duration

Total Fwd Packets

Flow Bytes/s

Fwd Packet Length Mean

SYN Flag Count
