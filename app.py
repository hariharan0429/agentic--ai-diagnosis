import streamlit as st
from main import run_system

st.set_page_config(page_title="AI Diagnosis Chatbot")

st.title("🧠 Interactive Diagnosis Chatbot")
st.warning("⚠️ Educational use only")

# Session state
if "step" not in st.session_state:
    st.session_state.step = 0
    st.session_state.symptoms = ""
    st.session_state.vitals = {}
    st.session_state.labs = {}

# Chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# Input
user_input = st.chat_input("Type your response...")

if user_input:

    # Show user message
    st.session_state.messages.append({"role": "user", "content": user_input})

    with st.chat_message("user"):
        st.write(user_input)

    # STEP LOGIC
    if st.session_state.step == 0:
        st.session_state.symptoms = user_input
        reply = "Do you have breathlessness? (yes/no)"
        st.session_state.step = 1

    elif st.session_state.step == 1:
        reply = "Enter SpO2 value (e.g., 92)"
        st.session_state.step = 2

    elif st.session_state.step == 2:
        st.session_state.vitals["spo2"] = int(user_input)
        reply = "Enter temperature (°C)"
        st.session_state.step = 3

    elif st.session_state.step == 3:
        st.session_state.vitals["temperature"] = float(user_input)
        reply = "Enter WBC count"
        st.session_state.step = 4

    elif st.session_state.step == 4:
        st.session_state.labs["wbc"] = int(user_input)
        reply = "Enter D-dimer (normal/high)"
        st.session_state.step = 5

    elif st.session_state.step == 5:
        st.session_state.labs["d_dimer"] = user_input

        # 🔥 Run AI system
        result = run_system(
            st.session_state.symptoms,
            st.session_state.vitals,
            st.session_state.labs
        )

        reply = f"""
### 🧾 Diagnosis Result

**Confidence:**
{result['confidence']}

**Evidence For:**
{result['evidence_for']}

**Next Step:**
{result['next_step']}

**Bias Check:**
{result['bias']}
"""

        st.session_state.step = 0  # restart

    # Show bot reply
    with st.chat_message("assistant"):
        st.markdown(reply)

    st.session_state.messages.append({"role": "assistant", "content": reply})
