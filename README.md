# IoT-Based Crop Recommendation System 🌱

*Empowering farmers with real-time, data-driven crop recommendations using IoT and continuous machine learning.*

## 📊 Overview

This notebook leverages IoT sensor data and machine learning to recommend crops, adapting continuously with farmer feedback for smarter agriculture.

## 🖼️ Project Flowchart & Logo

- **Add your flowchart here:**  
  `docs/flowchart.png`

- **Add your logo here:**  
  `docs/logo.png`

## 🚀 Features

1. Collects and preprocesses sensor data (N, P, K, temperature, humidity, pH, rainfall).
2. Trains a Random Forest model for initial crop recommendations.
3. Supports continuous learning with online updates.
4. Simulates IoT readings and farmer feedback.
5. Saves historical data for retraining.
6. Includes a Streamlit UI for user interaction.

## 📂 File Structure

```
project-root/
│
├── Crop_recommendation.csv           # Dataset
├── IoT_Crop_Recommendation.ipynb     # Main notebook
├── sensor_history.csv                # Historical data (auto-generated)
├── scaler.joblib                     # Scaler (auto-generated)
├── label_encoder.joblib              # Label encoder (auto-generated)
├── initial_model.joblib              # Initial model (auto-generated)
├── online_model.joblib               # Online model (auto-generated)
├── docs/
│   ├── flowchart.png                 # (Add your flowchart here)
│   ├── logo.png                      # (Add your logo here)
│   └── technical_documentation.pdf   # Technical writing (PDF)
├── ui/
│   └── streamlit_app.py              # Streamlit UI script
└── README.md                         # This file
```

## ⚙️ Setup & Usage

1. **Install dependencies:**
   ```
   pip install pandas numpy scikit-learn joblib river streamlit
   ```

2. **Add your dataset:**  
   Place `Crop_recommendation.csv` in the project root.

3. **Open the notebook:**  
   ```
   jupyter notebook IoT_Crop_Recommendation.ipynb
   ```

4. **Run all cells:**  
   Follow the markdown instructions in each section.

5. **Launch the Streamlit UI:**  
   ```
   streamlit run ui/streamlit_app.py
   ```

## 📝 Notebook Sections

- **Step 1:** Load and preprocess data.
- **Step 2:** Train initial model.
- **Step 3:** Set up continuous learning.
- **Step 4:** Simulate IoT device and feedback.

## 📑 Technical Documentation

You’ll find detailed technical writing and system explanations in:  
`docs/technical_documentation.pdf`

## 🎬 Demo Video

Watch the system in action:  
[Demo Video Link Here] (Replace with your actual video link)

## 🚧 Future Improvements

- Integrate real IoT hardware.
- Add more advanced models.
- Expand sensor types.
- Build a web dashboard.

## 📞 Contact

- *Phone:* +254 7XX XXX XXX  
- *Email:* yourname@email.com

Let me know if you want to tweak anything or need help with your demo video section! 😊
