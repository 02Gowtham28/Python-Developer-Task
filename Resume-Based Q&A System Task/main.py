# Standard library
import os

# Third-party packages
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional
from dotenv import load_dotenv

# LangChain & Gemini
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableMap
from langchain_core.output_parsers import StrOutputParser
from langchain_google_genai import ChatGoogleGenerativeAI

# Load environment variables
load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
if not GOOGLE_API_KEY:
    raise RuntimeError("GOOGLE_API_KEY not set in .env")

# ✅ Corrected Gemini model path
llm = ChatGoogleGenerativeAI(
    model="models/gemini-2.5-pro",  # ✅ fixed model name
    temperature=0.3,
    google_api_key=GOOGLE_API_KEY
)

# Sample Resume Text
MOCK_RESUME_CONTENT = """
Gowtham R
Data Analyst

Summary:
Detail-oriented Data Analyst with hands-on experience in SQL, Excel, Power BI, and Python for solving real-world business problems. Skilled in transforming raw data into actionable insights through data cleaning, visualization, and statistical analysis. Proven ability to develop interactive dashboards and communicate findings clearly to stakeholders. Passionate about data storytelling, pattern recognition, and supporting business decisions with evidence-backed analytics.

Experience:
- Data Analytics Intern Acciojob, Hyderabad (Remote) Dec 2024 – June 2025 | Built and deployed interactive dashboards in Power BI using Olympics and Walmart datasets, enabling visualization of key business insights like revenue trends, participation metrics, and gender distribution across 100+ years. Applied SQL, Excel, and Python for data cleaning and analysis, improving data quality and insight accuracy by over 30% across multiple real-world case projects. 
- Data Science Intern   June 2024 NEOWEP Software Technology, Dharmapuri | Engineered a real-time gender and age detection system using OpenCV, achieving a 20 percent accuracy improvement through optimized algorithms. Enhanced database performance by implementing efficient data storage and indexing techniques, reducing query times by 15%. 


Skills:
Data Analysis: Python (Pandas, NumPy), SQL, Excel, R 
Data Visualization: Power BI, Tableau, Matplotlib, Seaborn 
Databases: MySQL, Relational Database Design, Indexing 
Machine Learning: Scikit-learn, TensorFlow (Basics), OpenCV 
Techniques: Regression, Hypothesis Testing, Exploratory Data Analysis, Outlier 
Detection 
Soft Skills: Strong communication & presentation, Problem-solving mindset, Team 
collaboration, Time management, Quick adaptability 


Education:
- B.E. in Data Science, Annamalai University (2025)
"""

# LangChain Prompt Template
template = """
You are a helpful AI assistant trained to answer questions strictly from resume content.
If the answer is not in the resume, respond with "Information not found."

Resume:
---------------------
{resume}
---------------------

Question: {query}
Answer:
"""

prompt = PromptTemplate.from_template(template)

# Chain Setup
chain = (
    RunnableMap({"resume": lambda x: MOCK_RESUME_CONTENT, "query": lambda x: x["query"]})
    | prompt
    | llm
    | StrOutputParser()
)

# FastAPI Setup
app = FastAPI(
    title="Resume Q&A with LangChain + Gemini",
    description="Ask questions about a resume using LangChain and Google Gemini",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Request & Response Models
class QueryRequest(BaseModel):
    query: str

class QueryResponse(BaseModel):
    query: str
    response: str

# Endpoints
@app.get("/")
def root():
    return {"message": "Resume Q&A System (Gemini) is live. Use POST /query to ask questions."}

@app.post("/query", response_model=QueryResponse)
async def query_resume(request: QueryRequest):
    try:
        response = chain.invoke({"query": request.query})
        return QueryResponse(query=request.query, response=response)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Query failed: {str(e)}")
