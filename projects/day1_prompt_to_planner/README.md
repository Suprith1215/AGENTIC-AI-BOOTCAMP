# Day 1 Project: Goal Planner Agent 🧠

In this first hands-on project, you will move beyond simple "text generation" to build a **reasoning agent**. By connecting a Streamlit UI to the Gemini API, you’ll learn how to structure "system prompts" that force the AI to think like a planner rather than just a chatbot. You’ll master the flow of **Input → Reasoning → Structured Plan**, a foundational pattern for all autonomous agents.

## How to Run

1. **Create a Virtual Environment (Optional):**
   ```bash
   python -m venv venv
   # Windows:
   venv\Scripts\activate
   # Mac/Linux:
   source venv/bin/activate
   ```

2. **Install Dependencies:**
   ```bash
   pip install streamlit python-dotenv google-generativeai
   ```

3. **Set Up Your API Key:**
   - Create a `.env` file in this folder.
   - Copy the content from `.env.example`.
   - Paste your actual Google Gemini API key.

4. **Run the App:**
   ```bash
   streamlit run app.py
   ```
