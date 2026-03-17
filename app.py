import streamlit as st
from main import run_system

# Page config
st.set_page_config(page_title="CuraBot", page_icon="🩺", layout="wide")

# Custom CSS (Design)
st.markdown("""
<style>
body {
    background-color: #0f172a;
    color: white;
}
.chat-container {
    border-radius: 15px;
    padding: 15px;
    background-color: #1e293b;
}
.user-msg {
    background-color: #2563eb;
    padding: 10px;
    border-radius: 10px;
    margin: 5px;
}
.bot-msg {
    background-color: #334155;
    padding: 10px;
    border-radius: 10px;
    margin: 5px;
}
.title {
    text-align: center;
    font-size: 32px;
    font-weight: bold;
    color: #38bdf8;
}
.subtitle {
    text-align: center;
    color: #94a3b8;
}
</style>
""", unsafe_allow_html=True)

# Header
st.markdown('<div class="title">🩺 CuraBot</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">AI Health Assistant</div>', unsafe_allow_html=True)
st.write("---")

# Session state
if "messages" not in st.session_state:
    st.session_state.messages = []

if "step" not in st.session_state:
    st.session_state.step = 0
    st.session_state.symptoms = ""
    st.session_state.vitals = {}
    st.session_state.labs = {}

# Display messages
for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.markdown(f'<div class="user-msg">👤 {msg["content"]}</div>', unsafe_allow_html=True)
    else:
        st.markdown(f'<div class="bot-msg">🤖 {msg["content"]}</div>', unsafe_allow_html=True)

# Input box
user_input = st.chat_input("Type your response...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})

    # Step-based logic
    if st.session_state.step == 0:
        st.session_state.symptoms = user_input
        reply = "What other symptoms do you have?"
        st.session_state.step = 1

    elif st.session_state.step == 1:
        reply = "Enter SpO2 level (%)"
        st.session_state.step = 2

    elif st.session_state.step == 2:
        st.session_state.vitals["spo2"] = int(user_input)
        reply = "Enter body temperature (°C)"
        st.session_state.step = 3

    elif st.session_state.step == 3:
        st.session_state.vitals["temperature"] = float(user_input)
        reply = "Enter WBC count"
        st.session_state.step = 4

    elif st.session_state.step == 4:
        st.session_state.labs["wbc"] = int(user_input)
        reply = "Enter D-Dimer (normal/high)"
        st.session_state.step = 5

    elif st.session_state.step == 5:
        st.session_state.labs["d_dimer"] = user_input

        # Run AI
        result = run_system(
            st.session_state.symptoms,
            st.session_state.vitals,
            st.session_state.labs
        )

        reply = f"""
🧾 **Diagnosis Result**

📊 Confidence: {result['confidence']}

📌 Evidence: {result['evidence_for']}

➡️ Next Step: {result['next_step']}

⚖️ Bias Check: {result['bias']}
"""
        st.session_state.step = 0

    st.session_state.messages.append({"role": "assistant", "content": reply})
    st.rerun()
