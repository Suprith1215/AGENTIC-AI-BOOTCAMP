# 🚀 Installation Guide: From Scratch

Follow these steps to set up your computer for the Agentic AI Bootcamp.

---

## 1️⃣ Install Python (The Language)

Python is the programming language we will use.

### **Windows**
1.  Go to [python.org/downloads](https://www.python.org/downloads/).
2.  Click **"Download Python 3.x.x"** (latest version).
3.  **⚠️ CRITICAL STEP:** When the installer opens, check the box that says **"Add Python to PATH"**.
4.  Click "Install Now".

### **Mac**
1.  Go to [python.org/downloads](https://www.python.org/downloads/).
2.  Download the macOS installer.
3.  Run the package and follow instructions.
4.  (Optional) If you use Homebrew: `brew install python`

### **Verify Installation**
Open your terminal (Command Prompt or PowerShell) and type:
```bash
python --version
# or
python3 --version
```
If you see something like `Python 3.10.x`, you are good!

---

## 2️⃣ Install VS Code (The Editor)

Visual Studio Code is where we will write our code.

1.  Go to [code.visualstudio.com](https://code.visualstudio.com/).
2.  Download the version for your OS (Windows/Mac/Linux).
3.  Install it.
4.  **Recommended Extensions:** Open VS Code, go to the "Extensions" tab (square icon on left), and install:
    *   **Python** (by Microsoft)
    *   **Pylance** (by Microsoft)

---

## 3️⃣ Install Git & GitHub Setup

Git helps us save and share code.

### **Install Git**
*   **Windows:** Download from [git-scm.com](https://git-scm.com/download/win). Use default settings.
*   **Mac:** Open Terminal and type `git`. If not installed, it will ask to install Xcode Command Line Tools (say yes).

### **Sign Up for GitHub**
1.  Go to [github.com](https://github.com/).
2.  Create a free account.
3.  **Configure Git on your computer:**
    Open your terminal and run these commands (replace with your info):
    ```bash
    git config --global user.name "Your Name"
    git config --global user.email "your.email@example.com"
    ```

---

## 4️⃣ Set Up the Project

Now let's get the bootcamp code.

1.  **Clone the Repo:**
    ```bash
    git clone https://github.com/your-repo-url/agentic-ai-bootcamp.git
    cd agentic-ai-bootcamp
    ```

2.  **Create a Virtual Environment:**
    (This keeps your project clean)
    *   **Windows:** `python -m venv venv`
    *   **Mac/Linux:** `python3 -m venv venv`

3.  **Activate the Environment:**
    *   **Windows:** `venv\Scripts\activate`
    *   **Mac/Linux:** `source venv/bin/activate`
    *(You should see `(venv)` in your terminal now)*

---

## 5️⃣ Install Python Packages (Pip)

We need specific libraries for AI agents.

1.  Make sure your virtual environment is active (see step 4).
2.  Run:
    ```bash
    pip install -r requirements.txt
    ```
    *(If you don't have a requirements file yet, run: `pip install streamlit google-generativeai python-dotenv crewai langchain`)*

---

## ✅ You're Ready!

Test your setup by running:
```bash
streamlit hello
```
If a web page opens, you did it! 🎉
