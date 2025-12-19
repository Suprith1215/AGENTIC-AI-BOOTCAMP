# 📋 Evaluation Checklist for Capstone Projects

Use this checklist to grade your final project or peer-review others.

## 🧠 Agent Intelligence (40%)
- [ ] **Role Adherence:** Does the agent stay in character (e.g., Pirate, Tutor)?
- [ ] **Reasoning:** Does the agent break down complex queries logically?
- [ ] **Memory:** Does it remember context from previous messages in the session?
- [ ] **Tool Use:** Does it correctly identify when to use a tool (Calculator, Search)?

## 🛠️ Technical Implementation (30%)
- [ ] **Modular Code:** Is the code organized into `agents/`, `tools/`, etc.?
- [ ] **Error Handling:** Does the app crash on empty input or API errors?
- [ ] **API Security:** Are keys stored in `.env` or `st.secrets`, not hardcoded?
- [ ] **Efficiency:** does it avoid unnecessary API calls?

## 🎨 User Experience (UI/UX) (20%)
- [ ] **Clarity:** Are instructions and buttons clear to the user?
- [ ] **Feedback:** Does it show "Thinking..." or spinners while processing?
- [ ] **Formatting:** Is the output easy to read (Markdown, Bullet points)?
- [ ] **Visuals:** Are emojis or layout used effectively?

## 🛡️ Responsible AI (10%)
- [ ] **Safety:** Does it refuse harmful requests?
- [ ] **Transparency:** Does it admit when it doesn't know something?
- [ ] **Disclaimer:** Is there a note stating "AI can make mistakes"?

---

## 🏆 Bonus Points
- [ ] **Creative Theme:** Unique and engaging concept.
- [ ] **Multi-Agent:** Uses more than one agent (e.g., Planner + Executor).
- [ ] **Advanced Tools:** Uses a new API (Weather, Finance, etc.).
