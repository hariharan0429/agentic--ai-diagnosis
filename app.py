import streamlit as st
from main import run_system

st.set_page_config(page_title="Agentic AI Chatbot")

st.title("🧠 AI Diagnosis Chatbot")
st.warning("⚠️ For education only. Not real medical advice.")

# Chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display old messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# User input
user_input = st.chat_input("Enter symptoms or updates...")

if user_input:
    # Show user message
    st.session_state.messages.append({"role": "user", "content": user_input})

    with st.chat_message("user"):
        st.write(user_input)

    # Simple parsing (you can improve later)
    vitals = {"spo2": 95, "temperature": 37}
    labs = {"wbc": 8000, "d_dimer": "normal"}

    # Run your AI system
    result = run_system(user_input, vitals, labs)

    # Format response
    response = f"""
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

    # Show bot response
    with st.chat_message("assistant"):
        st.markdown(response)

    st.session_state.messages.append({"role": "assistant", "content": response})
