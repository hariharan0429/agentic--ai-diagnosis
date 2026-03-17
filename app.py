import streamlit as st
from main import run_system

st.set_page_config(page_title="Agentic AI Diagnosis Tutor")

st.title("🧠 Agentic AI Differential Diagnosis Tutor")
st.warning("⚠️ This system is for medical education only. Not for real diagnosis.")

symptoms = st.text_input("Enter symptoms (comma separated)")

col1, col2 = st.columns(2)

with col1:
    spo2 = st.number_input("SpO2 (%)", value=98)
    temp = st.number_input("Temperature (°C)", value=37)

with col2:
    wbc = st.number_input("WBC count", value=8000)
    d_dimer = st.selectbox("D-Dimer", ["normal", "high"])

if st.button("Run Diagnosis"):
    result = run_system(
        symptoms,
        {"spo2": spo2, "temperature": temp},
        {"wbc": wbc, "d_dimer": d_dimer}
    )

    st.subheader("📊 Confidence Levels")
    st.json(result["confidence"])

    st.subheader("✅ Evidence For")
    st.json(result["evidence_for"])

    st.subheader("❌ Evidence Against")
    st.json(result["evidence_against"])

    st.subheader("➡️ Next Step")
    st.success(result["next_step"])

    st.subheader("⚠️ Bias Check")
    st.info(result["bias"])
