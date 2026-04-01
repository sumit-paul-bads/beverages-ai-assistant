🍹 Beverage AI Assistant

📌 Overview

Beverage AI Assistant is an AI-powered analytics tool that converts natural language questions into SQL queries and generates business insights from structured data.

The system allows users to interact with data using simple questions like:

- "Which brand has the highest margin?"
- "Top 5 brands by revenue"

---

🚀 Features

- 🧠 Natural Language → SQL (via Ollama LLM)
- 🗄️ Automatic query execution on structured data
- 📊 Dynamic result display
- 💡 Business insight generation
- ⚡ Fast and lightweight Streamlit UI

---

🏗️ Architecture

User Question
↓
LLM (Ollama - LLaMA3)
↓
SQL Generation
↓
DuckDB Execution
↓
Results
↓
Insight Generation

---

🧰 Tech Stack

- Python
- Streamlit (UI)
- DuckDB (Database)
- Pandas
- Ollama (LLaMA3) (Local LLM)

---

📂 Project Structure

beverage-ai-assistant/
│
├── app.py                 # Streamlit UI
├── llm_engine.py          # LLM → SQL + Insights
├── db_setup.py            # Data loading into DuckDB
├── query_engine.py        # SQL execution
├── data/
│   └── beverages.xlsx     # Dataset
├── requirements.txt
└── README.md

---

⚙️ How to Run

1. Clone the repository

git clone https://github.com/sumit-paul-bads/beverages-ai-assistant
cd beverages-ai-assistant

---

2. Install dependencies

pip install -r requirements.txt

---

3. Start Ollama (LLM)

Make sure Ollama is installed, then run:
ollama run llama3

---

4. Run the app

streamlit run app.py

---

💬 Example Queries

- Which brand has the highest margin?
- Top 5 brands by revenue
- Average margin by brand
- Total sales by brand

---

🧠 Key Challenges & Solutions

Problem: Incorrect SQL joins (LLM hallucination)
Solution: Used strict prompt engineering and rule-based SQL cleaning to enforce correct joins

Problem: Inconsistent SQL formatting
Solution: Applied post-processing to extract clean SQL output

---

💡 Key Learnings

- Prompt engineering is critical for structured outputs
- LLM outputs must always be validated
- Combining LLM + SQL requires strict schema control
- End-to-end pipeline design matters more than just model usage

---

🎥 Demo Video

https://drive.google.com/file/d/13ME9JvdF4ZxT3Q82-GjUDhhajBcPKgMc/view?usp=sharing

---

📈 Future Improvements

- Add visualization (charts)
- Deploy on cloud
- Support more complex queries
- Improve performance with caching

---

👤 Author

Sumit Paul

---

🏁 Conclusion

This project demonstrates how LLMs can be integrated with structured databases to create an intelligent analytics assistant, bridging the gap between business users and data systems.
