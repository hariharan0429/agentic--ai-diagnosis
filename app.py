import streamlit as st
from main import run_system

# Page setup
st.set_page_config(page_title="CuraBot", page_icon="🩺", layout="wide")

# 🎨 Custom CSS (Light + Gradient UI)
st.markdown("""
<style>
body {
    background: linear-gradient(to right, #e0f7fa, #ffffff);
}

.header {
    text-align: center;
    font-size: 40px;
    font-weight: bold;
    color: #0ea5e9;
}

.subheader {
    text-align: center;
    color: #64748b;
    margin-bottom: 20px;
}

.chat-box {
    background: white;
    padding: 15px;
    border-radius: 15px;
    margin-bottom: 10px;
    box-shadow: 0px 2px 8px rgba(0,0,0,0.1);
}

.user {
    background: #0ea5e9;
    color: white;
    padding: 10px;
    border-radius: 10px;
    margin: 5px;
    text-align: right;
}

.bot {
    background: #f1f5f9;
    color: black;
    padding: 10px;
    border-radius: 10px;
    margin: 5px;
}

.footer {
    text-align: center;
    color: gray;
    margin-top: 20px;
    font-size: 12px;
}
</style>
""", unsafe_allow_html=True)

# Header
st.markdown('<div class="header">🩺 CuraBot</div>', unsafe_allow_html=True)
st.markdown('<div class="subheader">Smart AI Health Assistant</div>', unsafe_allow_html=True)

# Session state
if "messages" not in st.session_state:
    st.session_state.messages = []

if "step" not in st.session_state:
    st.session_state.step = 0
    st.session_state.symptoms = ""
    st.session_state.vitals = {}
    st.session_state.labs = {}

# Display chat
for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.markdown(f'<div class="user">👤 {msg["content"]}</div>', unsafe_allow_html=True)
    else:
        st.markdown(f'<div class="bot">🤖 {msg["content"]}</div>', unsafe_allow_html=True)

# Input
user_input = st.chat_input("Type your response...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})

    # Step logic
    if st.session_state.step == 0:
        st.session_state.symptoms = user_input
        reply = "🤖 What other symptoms do you have?"
        st.session_state.step = 1

    elif st.session_state.step == 1:
        reply = "📊 Enter SpO2 level (%)"
        st.session_state.step = 2

    elif st.session_state.step == 2:
        st.session_state.vitals["spo2"] = int(user_input)
        reply = "🌡️ Enter body temperature (°C)"
        st.session_state.step = 3

    elif st.session_state.step == 3:
        st.session_state.vitals["temperature"] = float(user_input)
        reply = "🧪 Enter WBC count"
        st.session_state.step = 4

    elif st.session_state.step == 4:
        st.session_state.labs["wbc"] = int(user_input)
        reply = "🧬 Enter D-Dimer (normal/high)"
        st.session_state.step = 5

    elif st.session_state.step == 5:
        st.session_state.labs["d_dimer"] = user_input

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

# Footer
st.markdown('<div class="footer">© 2026 CuraBot | AI Healthcare Assistant</div>', unsafe_allow_html=True)
