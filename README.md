
# IoT-Based Crop Recommendation System 🌱

*Empowering farmers with real-time, data-driven crop recommendations using IoT and continuous machine learning.*

## 📊 Overview

This notebook uses IoT sensor data and machine learning to recommend crops, adapting continuously with farmer feedback.

## 🖼️ Project Flowchart & Logo

- **Add your flowchart here:**  
  ``

- **Add your logo here:**  
  ``

## 🚀 Features

1. Collects and preprocesses sensor data (N, P, K, temp, humidity, pH, rainfall).
2. Trains a Random Forest model for initial crop recommendations.
3. Supports continuous learning with online updates.
4. Simulates IoT readings and farmer feedback.
5. Saves historical data for retraining.

## 📂 File Structure

```
project-root/
│
├── Crop_recommendation.csv        # Dataset
├── IoT_Crop_Recommendation.ipynb  # Main notebook
├── sensor_history.csv             # Historical data (auto-generated)
├── scaler.joblib                  # Scaler (auto-generated)
├── label_encoder.joblib           # Label encoder (auto-generated)
├── initial_model.joblib           # Initial model (auto-generated)
├── online_model.joblib            # Online model (auto-generated)
├── docs/
│   ├── flowchart.png              # (Add your flowchart here)
│   └── logo.png                   # (Add your logo here)
└── README.md                      # This file
```

## ⚙️ Setup & Usage

1. **Install dependencies:**
   ```
   pip install pandas numpy scikit-learn joblib river
   ```

2. **Add your dataset:**  
   Place `Crop_recommendation.csv` in the project root.

3. **Open the notebook:**  
   ```
   jupyter notebook IoT_Crop_Recommendation.ipynb
   ```

4. **Run all cells:**  
   Follow the markdown instructions in each section.

## 📝 Notebook Sections

- **Step 1:** Load and preprocess data.
- **Step 2:** Train initial model.
- **Step 3:** Set up continuous learning.
- **Step 4:** Simulate IoT device and feedback.

## 🚧 Future Improvements

- Integrate real IoT hardware.
- Add more advanced models.
- Expand sensor types.
- Build a web dashboard.
