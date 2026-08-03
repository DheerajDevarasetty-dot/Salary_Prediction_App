import streamlit as st
import joblib
import numpy as np

try:
    model = joblib.load("salary_model.pkl")
except Exception as e:
    st.error(f"❌ Model loading failed: {e}")
    st.stop()

st.set_page_config(page_title="Salary Predictor", layout="centered")
st.title("💼 Salary Prediction App")
st.write("Predict salary based on experience")

experience = st.slider("Years of Experience", 0.0, 20.0, 1.0)

input_data = np.array([[experience]])

if st.button("Predict Salary"):
    try:
        prediction = model.predict(input_data)
        salary = round(prediction[0], 2)

        st.success(f"💰 Predicted Salary: ₹ {salary}")

    except Exception as e:
        st.error(f"⚠️ Prediction Error: {e}")

st.markdown("---")
st.subheader("📊 Input Summary")
st.write(f"Experience: {experience} years")
#to run: python -m streamlit run app.py