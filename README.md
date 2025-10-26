# 🎯 AI Career Counsellor

An **AI-powered career guidance assistant** built with **Rasa** (for natural language understanding and dialogue management) and **Streamlit** (for an interactive user interface).  
The system analyzes user interests (like “I love AI and ML”) and suggests the most suitable career path — similar to a personalized ChatGPT-style counsellor.

---

## 🚀 Features

- 💬 Chatbot powered by **Rasa NLU** for understanding user input.
- 🧭 Smart recommendation engine for career paths.
- 🎨 Beautiful **Streamlit** frontend UI.
- 🧱 Modular project structure with clear separation of backend and frontend.
- ⚙️ Works entirely offline — **no API keys** required.

---

## 🗂️ Folder Structure

```
AI-Career-Counsellor/
│
├── app.py                    # Streamlit frontend app
├── careermap.json            # JSON file mapping interests → careers
├── requirements.txt          # Python dependencies
│
├── rasa_backend/             # Rasa project folder
│   ├── actions/
│   │   ├── __init__.py       # Marks the folder as a Python package
│   │   ├── actions.py        # Contains custom chatbot actions
│   │   └── preprocess.py     # Optional: data preprocessing
│   │
│   ├── data/
│   │   ├── nlu.yml           # NLU training examples
│   │   ├── stories.yml       # Training stories
│   │   ├── rules.yml         # Rules for predictable responses
│   │   └── models/           # Trained Rasa models saved here
│   │
│   ├── config.yml            # Pipeline and policy configuration
│   ├── domain.yml            # Intents, entities, responses, actions
│   └── endpoints.yml         # Connects to custom actions
│
└── README.md
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone or Download the Repository
```bash
git clone https://github.com/<your-username>/AI-Career-Counsellor.git
cd AI-Career-Counsellor
```

### 2️⃣ Create and Activate Virtual Environment
#### For Windows:
```bash
py -3.10 -m venv venv310
venv310\Scripts\activate
```

#### For Mac/Linux:
```bash
python3 -m venv venv310
source venv310/bin/activate
```

---

### 3️⃣ Install Required Dependencies
```bash
pip install -r requirements.txt
```

---

### 4️⃣ Train the Rasa Model
Move inside the backend folder and train:
```bash
cd "rasa_backend"
rasa train
```

This will create a trained model inside the `models/` folder.

---

### 5️⃣ Run the Rasa Action Server
```bash
rasa run actions
```

---

### 6️⃣ Run the Rasa Server (in a new terminal)
```bash
rasa run --enable-api --cors "*"
```

---

### 7️⃣ Run the Streamlit App
Open a new terminal at the **project root** (`AI-Career-Counsellor/`) and run:
```bash
streamlit run app.py
```

Now open the local URL (shown in terminal, e.g., `http://localhost:8501`) in your browser.

---

## 🧩 How It Works

1. User enters a message in the Streamlit chatbox (e.g., *“I love AI and ML”*).
2. Streamlit sends the text to the Rasa backend.
3. Rasa predicts the intent (e.g., `user_interest`) and calls the appropriate action (`action_recommend_career`).
4. The action looks up `careermap.json` to find the best career match.
5. Streamlit displays the response beautifully in a chat-like UI.

---

## 🧠 Example Interactions

| User Message | Bot Response |
|---------------|---------------|
| I love AI and ML | You should explore careers in Data Science, Machine Learning, or AI Engineering. |
| I enjoy designing websites | You might be interested in Front-End or UI/UX Development. |
| I like solving logical problems | A career in Software Engineering or Cybersecurity could be a great fit. |

---

## 🧰 Tech Stack

- **Rasa** — Conversational AI framework  
- **Streamlit** — Interactive Python web app framework  
- **Python 3.10+** — Core programming language  
- **JSON** — For career data mapping  

---

## 🌟 Future Enhancements

- Add user authentication to save career results.
- Integrate voice-based conversation.
- Visualize career paths with interactive graphs.
- Deploy on Hugging Face or Streamlit Cloud.

---

## 🧑‍💻 Author

**Shivani Naroju**  
AI & ML Enthusiast | B.Tech CSE Student  


---

