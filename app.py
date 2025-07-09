import streamlit as st
import numpy as np
import joblib

# Load the trained model and the LabelEncoder
model = joblib.load("decision_tree_model.pkl")
encoder = joblib.load("encoder.pkl")  # Save your encoder and load here

# Title
st.title("Fault Prediction System")
st.write("Enter the electrical parameters to predict the type of fault.")

# Input fields
Ia = st.number_input("Current in Line A (Ia)", value=0.0)
Ib = st.number_input("Current in Line B (Ib)", value=0.0)
Ic = st.number_input("Current in Line C (Ic)", value=0.0)
Va = st.number_input("Voltage in Line A (Va)", value=0.0)
Vb = st.number_input("Voltage in Line B (Vb)", value=0.0)
Vc = st.number_input("Voltage in Line C (Vc)", value=0.0)

# G, C, B, A (static for now)
G = 0
C = 0
B = 0
A = 0

# Prepare input data
input_data = np.array([[G, C, B, A, Ia, Ib, Ic, Va, Vb, Vc]])

# Predict
if st.button("Predict Fault Type"):
    prediction = model.predict(input_data)[0]  # Numeric label
    fault_description = encoder.inverse_transform([prediction])[0]  # Convert to original label

    st.success(f"The predicted fault type is: *{fault_description}*")