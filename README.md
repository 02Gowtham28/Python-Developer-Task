# Python-Developer-Task
# 🧠 Resume-Based Q&A System using LLMs (FastAPI + Gemini + LangChain)

This project is a resume-driven **question-answering API** powered by **Google Gemini (via LangChain)** and served with **FastAPI**. It answers questions based **strictly on your own resume**, using structured prompting and no hallucination.

---

## 📌 Objective

- ✅ Use your personal resume as the knowledge base.
- ✅ Extract and embed resume content using LangChain.
- ✅ Accept a **POST** request with a query in JSON.
- ✅ Retrieve relevant resume data and respond using an **LLM (Gemini)**.
- ✅ Response is **grounded only in the resume**.

---

## 📸 Demo Screenshots

### 🔹 FastAPI Swagger UI Interface

<img width="1913" height="1001" alt="Screenshot 2025-08-07 184616" src="https://github.com/user-attachments/assets/7f4cd333-7758-4889-b877-d312ee69ca29" />


---

### 🔹 Sending Query via `/query` Endpoint

<img width="1885" height="828" alt="Screenshot 2025-08-07 184630" src="https://github.com/user-attachments/assets/ba31d6c6-e3cb-4c8d-bb31-bd3e113d2375" />


---

### 🔹 Server Response Based on Resume

<img width="1880" height="815" alt="Screenshot 2025-08-07 184649" src="https://github.com/user-attachments/assets/4da40335-8e2f-471c-851a-95f9edb47287" />



---

## 🛠️ Tech Stack

| Component        | Tech Used                |
|------------------|---------------------------|
| Language         | Python 3.10+              |
| Framework        | FastAPI                   |
| LLM              | Google Gemini (`langchain-google-genai`) |
| Prompting Tool   | LangChain                 |
| Deployment Tool  | Uvicorn                   |
| Config Mgmt      | python-dotenv             |

---

## 💼 Sample Resume Used

```text
Gowtham R
Data Analyst with hands-on experience in Python, SQL, Power BI, Excel, and real-world business problem solving. Built dashboards, analyzed Olympic and Walmart datasets, and developed real-time systems using OpenCV. Passionate about data storytelling and analytics.
```

---

## 📥 Sample Input & Output

### ✅ Input (POST `/query`)
```json
{
  "query": "what is your education"
}
```

### ✅ Output
```json
{
  "query": "what is your education",
  "response": "B.E. in Data Science, Annamalai University (2025)"
}
```

---

## 📁 File Structure

```
.
├── main.py              # FastAPI app and LangChain logic
├── .env                 # Contains GOOGLE_API_KEY
├── requirements.txt     # All Python dependencies
├── README.md            # This file
├── Screenshot 2025-08-07 184616.png  # Swagger UI
├── Screenshot 2025-08-07 184630.png  # POST Request
└── Screenshot 2025-08-07 184649.png  # Response Output
```

---

## ⚙️ Setup & Run Locally

### 1. Clone this repo

```bash
git clone https://github.com/your-username/resume-qa-llm.git
cd resume-qa-llm
```

### 2. Set up a virtual environment

```bash
python -m venv venv
venv\Scripts\activate       # Windows
# or
source venv/bin/activate   # Linux/Mac
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Create a `.env` file

```
GOOGLE_API_KEY=your_google_api_key_here
```

> 🔐 Do NOT commit `.env` to GitHub!

### 5. Run the app

```bash
uvicorn main:app --reload
```

Now open your browser at:  
📎 [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

## 🧠 Prompt Format Used

```
You are a helpful AI assistant trained to answer questions strictly from resume content.
If the answer is not in the resume, respond with "Information not found."

Resume:
---------------------
{resume}
---------------------

Question: {query}
Answer:
```

---

## 📎 License

This project is open-source under the [MIT License](LICENSE).

---

## 👨‍💻 Author

**Gowtham R**  
📫 [LinkedIn]: https://www.linkedin.com/in/28gowtham/ • [GitHub]: https://github.com/02Gowtham28/
