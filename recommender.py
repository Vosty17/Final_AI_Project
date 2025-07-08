import streamlit as st
import joblib
import numpy as np
import pandas as pd

# Setting page config
st.set_page_config(
    page_title="Crop Recommendation System",
    page_icon="🌱",
    layout="wide"
)

# Load saved models and encoders
@st.cache_resource
def load_models():
    model = joblib.load('initial_model.joblib')
    scaler = joblib.load('scaler.joblib')
    le = joblib.load('label_encoder.joblib')
    return model, scaler, le

model, scaler, le = load_models()

# Sidebar with user inputs
st.sidebar.header("🌾 Input Sensor Data")
st.sidebar.write("Adjust the sliders to match your field conditions")

n_input = st.sidebar.slider('Nitrogen (N)', 0, 140, 50)
p_input = st.sidebar.slider('Phosphorus (P)', 5, 145, 30)
k_input = st.sidebar.slider('Potassium (K)', 5, 205, 20)
temp_input = st.sidebar.slider('Temperature (°C)', 8, 44, 25)
humidity_input = st.sidebar.slider('Humidity (%)', 14, 99, 60)
ph_input = st.sidebar.slider('pH', 3.5, 9.9, 6.5)
rainfall_input = st.sidebar.slider('Rainfall (mm)', 20, 300, 100)

# Main content area
st.title("🌱 Smart Crop Recommendation System")
st.markdown("""
This AI-powered system recommends the best crop to plant based on your soil and weather conditions.
""")

# Create input dataframe
input_data = pd.DataFrame({
    'N': [n_input],
    'P': [p_input],
    'K': [k_input],
    'temperature': [temp_input],
    'humidity': [humidity_input],
    'ph': [ph_input],
    'rainfall': [rainfall_input]
})

# Display input data
with st.expander("📊 Current Input Parameters"):
    st.dataframe(input_data.style.highlight_max(axis=0))

# Make prediction
if st.button("🚜 Get Crop Recommendation"):
    # Scale input data
    scaled_input = scaler.transform(input_data)
    
    # Make prediction
    prediction = model.predict(scaled_input)
    proba = model.predict_proba(scaled_input)
    
    # Get top 3 predictions
    top3_idx = np.argsort(proba[0])[-3:][::-1]
    top3_crops = le.inverse_transform(top3_idx)
    top3_probs = proba[0][top3_idx]
    
    # Display results
    st.success(f"**Recommended Crop:** {le.inverse_transform(prediction)[0]}")
    
    st.subheader("🌾 Top 3 Recommendations")
    cols = st.columns(3)
    for i, (crop, prob) in enumerate(zip(top3_crops, top3_probs)):
        with cols[i]:
            st.metric(
                label=crop,
                value=f"{prob:.1%} confidence",
                help=f"Suitability score for {crop}"
            )
    
    # Show probability distribution
    st.subheader("📈 Full Crop Probability Distribution")
    prob_df = pd.DataFrame({
        'Crop': le.classes_,
        'Probability': proba[0]
    }).sort_values('Probability', ascending=False)
    
    st.bar_chart(prob_df.set_index('Crop'))

# Add footer
st.markdown("---")
st.markdown("""
**How it works:**
1. Adjust the sliders to match your field conditions
2. Click the recommendation button
3. See AI-powered crop suggestions

*Model trained on crop recommendation dataset with Random Forest algorithm*
""")