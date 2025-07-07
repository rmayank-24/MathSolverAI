# 🧮 MathSolverAI

An AI-powered chatbot built with Streamlit and LangChain that helps users solve math problems step-by-step using natural language.

🟢 **Live Demo**: [https://mathsolverchatbot.streamlit.app](https://mathsolverchatbot.streamlit.app)

---

## ✨ Features

- 💬 Chat-based interface for math Q&A
- 🧠 Powered by **Google Gemini** via `langchain_google_genai`
- 📚 Handles algebra, calculus, trigonometry, word problems, and more
- 🖼️ Minimal and interactive UI with **Streamlit**
- 🔄 Real-time responses with LangChain's callback handler

---



---

## 🧰 Tech Stack

| Layer         | Tech Used                        |
|---------------|----------------------------------|
| Frontend UI   | Streamlit                        |
| LLM Interface | LangChain + Google Gemini        |
| LLM Backend   | Gemini Pro / Gemini 1.5 (via API)|
| Hosting       | Streamlit Cloud                  |

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/rmayank-24/MathSolverAI.git
cd MathSolverAI
```

### 2. Create and activate virtual environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Add your environment variables

Create a `.env` file in the root directory and add your **Google Gemini API key**:

```env
GOOGLE_API_KEY=your_gemini_api_key_here
```

> Get your API key from: https://aistudio.google.com/app/apikey

### 5. Run the app locally

```bash
streamlit run app.py
```

---

## 🗂️ Project Structure

```
MathSolverAI/
├── app.py                 # Main Streamlit app
├── .env.example           # Example env file
├── requirements.txt       # Python dependencies
├── assets/                # (Optional) Images/screenshots
└── README.md
```

---

## 🔐 Environment Variables

| Variable         | Description                   |
|------------------|-------------------------------|
| `GOOGLE_API_KEY` | Your Google Gemini API key    |

---

## 📈 Future Plans

- [ ] Add LaTeX rendering for better math formatting
- [ ] Voice input/output
- [ ] Problem-solving history with download option
- [ ] Option to switch between Gemini & OpenAI backends

---

## 🧑‍💻 Author

**Mayank Rathi**  
GitHub: [@rmayank-24](https://github.com/rmayank-24)  
LinkedIn: [mayank-rathi24](https://www.linkedin.com/in/mayank-rathi24/)

---

## 📄 License

Licensed under the [MIT License](LICENSE)

---

## ⭐️ Show Your Support

If you found this helpful, please give the repo a ⭐️ on [GitHub](https://github.com/rmayank-24/MathSolverAI)!
