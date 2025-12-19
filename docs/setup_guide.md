# 🚀 Getting Started Guide

Welcome to the Agentic AI Bootcamp! This guide will help you set up your environment and get ready for the sessions.

## 1️⃣ Prerequisites

Before we begin, make sure you have the following installed:

*   **Python 3.10 or higher:** [Download Python](https://www.python.org/downloads/)
*   **VS Code (Recommended):** [Download VS Code](https://code.visualstudio.com/)
*   **Git:** [Download Git](https://git-scm.com/downloads)

## 2️⃣ Clone the Repository

Open your terminal (Command Prompt, PowerShell, or Terminal) and run:

```bash
git clone https://github.com/yourusername/agentic-ai-bootcamp.git
cd agentic-ai-bootcamp
```

## 3️⃣ Create a Virtual Environment

It's best practice to use a virtual environment to keep your dependencies isolated.

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**Mac/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

You should see `(venv)` in your terminal prompt.

## 4️⃣ Install Dependencies

Install the required Python libraries:

```bash
pip install -r requirements.txt
```

## 5️⃣ Set Up API Keys 🔑

You will need API keys for Google Gemini (and optionally OpenAI/Serper).

1.  **Get Google Gemini Key:** [Google AI Studio](https://makersuite.google.com/app/apikey)
2.  **Create .env file:**
    *   Copy `env.example` to a new file named `.env`
    *   Open `.env` and paste your key: `GOOGLE_API_KEY=your_actual_key_here`

**⚠️ IMPORTANT:** Never share your `.env` file or commit it to GitHub!

## 6️⃣ Verify Setup

Run the verification script (Day 1 Project) to make sure everything works:

```bash
streamlit run projects/day1_prompt_to_planner/app.py
```

If a web page opens and the app runs, you are ready! 🎉
