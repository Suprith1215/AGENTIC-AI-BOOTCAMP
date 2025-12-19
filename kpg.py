"""
KPG – Knowledge & Planning Guide (AI Study Mentor)

Day 4 Capstone Project
- Agent Reasoning
- Memory
- Tools
- Responsible AI
- Streamlit UI
"""

import os
import json
import re
import streamlit as st
from datetime import datetime
from dotenv import load_dotenv

from agents.main_agent import AIAgent
from tools.basic_tools import calculator, search_web

# -----------------------------
# LOAD ENV
# -----------------------------
load_dotenv()

# -----------------------------
# APP CONFIGURATION
# -----------------------------
PROJECT_NAME = "KPG – AI Study Mentor"
PROJECT_DESCRIPTION = """
🎓 **KPG (Knowledge & Planning Guide)** helps engineering students learn better.

### Features
- 🧠 Remembers conversation
- 🛠️ Uses tools (Calculator, Study Plans)
- 📚 Explains step-by-step
- 🛡️ Safe & responsible AI
"""

# -----------------------------
# PAGE SETUP
# -----------------------------
st.set_page_config(
    page_title=PROJECT_NAME,
    page_icon="🎓",
    layout="wide"
)

# -----------------------------
# SESSION STATE
# -----------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

if "memory_enabled" not in st.session_state:
    st.session_state.memory_enabled = True

# -----------------------------
# HEADER
# -----------------------------
st.title(f"🎓 {PROJECT_NAME}")
st.markdown(PROJECT_DESCRIPTION)
st.markdown("---")

# -----------------------------
# SIDEBAR
# -----------------------------
with st.sidebar:
    st.header("⚙️ Agent Settings")

    persona = st.selectbox(
        "Select Personality",
        ["Study Buddy", "Code Tutor", "Helpful Assistant", "Custom"]
    )

    persona_map = {
        "Study Buddy": "You are a supportive study mentor for engineering students.",
        "Code Tutor": "You are a patient programming tutor who explains step by step.",
        "Helpful Assistant": "You are a friendly AI assistant.",
    }

    custom_persona = ""
    if persona == "Custom":
        custom_persona = st.text_area("Custom Personality")
    else:
        custom_persona = persona_map[persona]

    system_prompt = st.text_area(
        "System Prompt",
        value=f"""{custom_persona}
Explain concepts clearly.
Use simple language.
Encourage learning.
""",
        height=150
    )

    st.markdown("---")

    st.markdown("### 🧠 Memory")
    st.session_state.memory_enabled = st.checkbox("Enable Memory", True)
    if st.button("Clear Memory"):
        st.session_state.messages = []
        st.rerun()

    st.markdown("---")
    st.markdown("### 📊 Stats")
    st.metric("Messages", len(st.session_state.messages))

# -----------------------------
# INITIALIZE AGENT
# -----------------------------
agent = AIAgent(system_prompt=system_prompt)

if not agent.api_key:
    st.error("❌ GOOGLE_API_KEY missing")
    st.stop()

# -----------------------------
# CHAT DISPLAY
# -----------------------------
st.subheader("💬 Chat with KPG")

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])
        st.caption(msg["time"])

# -----------------------------
# USER INPUT
# -----------------------------
user_input = st.chat_input("Ask your question...")

if user_input:

    # Responsible AI guardrail
    if len(user_input) > 300:
        st.warning("⚠️ Please ask a shorter question.")
        st.stop()

    timestamp = datetime.now().strftime("%H:%M:%S")

    st.session_state.messages.append({
        "role": "user",
        "content": user_input,
        "time": timestamp
    })

    with st.chat_message("user"):
        st.write(user_input)
        st.caption(timestamp)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):

            response = None
            tool_used = None

            # -----------------------------
            # CALCULATOR TOOL
            # -----------------------------
            if any(op in user_input for op in ["+", "-", "*", "/", "="]):
                try:
                    expr = re.findall(r"[\d+\-*/(). ]+", user_input)[0]
                    response = f"🔢 Result: {calculator(expr)}"
                    tool_used = "Calculator"
                except:
                    pass

            # -----------------------------
            # STUDY PLAN TOOL
            # -----------------------------
            if not response and "study plan" in user_input.lower():
                subject = user_input.lower().replace("study plan", "").strip()
                response = f"""
📘 **Study Plan for {subject if subject else "your subject"}**

1️⃣ Learn basics  
2️⃣ Watch tutorials  
3️⃣ Practice problems  
4️⃣ Revise notes  
5️⃣ Solve previous questions  

Consistency is key 💪
"""
                tool_used = "Study Plan Tool"

            # -----------------------------
            # LLM RESPONSE
            # -----------------------------
            if not response:
                if st.session_state.memory_enabled:
                    context = "\n".join(
                        [f"{m['role']}: {m['content']}" for m in st.session_state.messages[-5:]]
                    )
                    response = agent.generate_response(user_input, context=context)
                else:
                    response = agent.generate_response(user_input)

            st.write(response)
            if tool_used:
                st.caption(f"🛠️ Tool used: {tool_used}")
            st.caption(timestamp)

    st.session_state.messages.append({
        "role": "assistant",
        "content": response,
        "time": timestamp
    })

    st.rerun()

# -----------------------------
# EXPORT CHAT
# -----------------------------
st.markdown("---")
if st.button("📥 Export Chat History"):
    chat_data = json.dumps(st.session_state.messages, indent=2)
    st.download_button(
        "Download Chat",
        chat_data,
        "kpg_chat_history.json",
        "application/json"
    )

# -----------------------------
# FOOTER
# -----------------------------
st.markdown("---")
st.caption("🚀 KPG – AI Study Mentor | Day 4 Capstone Project")
