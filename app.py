import streamlit as st
from main import run_system
import json

st.set_page_config(page_title="CuraBot", layout="wide")

# 🎨 UI STYLE
st.markdown("""
<style>
.main {
    background: linear-gradient(to right, #e0f7fa, #ffffff);
}
.chat-bubble {
    padding: 12px;
    border-radius: 12px;
    margin: 8px 0;
}
.user {
    background: #0ea5e9;
    color: white;
    text-align: right;
}
.bot {
    background: #f1f5f9;
}
</style>
""", unsafe_allow_html=True)

st.title("🩺 CuraBot - AI Diagnosis Assistant")
st.caption("Educational use only")

if "messages" not in st.session_state:
    st.session_state.messages = []

# Show chat
for msg in st.session_state.messages:
    role_class = "user" if msg["role"] == "user" else "bot"
    st.markdown(f'<div class="chat-bubble {role_class}">{msg["content"]}</div>', unsafe_allow_html=True)

# Input
user_input = st.chat_input("Enter symptoms (e.g. fever, cough)")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})

    result = run_system(user_input)

    reply = f"""
### 🧾 Diagnosis

📊 **Confidence:**  
{result['confidence']}

📌 **Evidence:**  
{result['evidence']}

➡️ **Next Step:**  
{result['next_step']}

🧠 **Reasoning:**  
{result['reasoning']}
"""

    reply += "\n\n```json\n" + json.dumps(result, indent=2) + "\n```"

    st.session_state.messages.append({"role": "assistant", "content": reply})
    st.rerun()
