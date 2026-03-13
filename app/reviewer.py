from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os

load_dotenv()

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    groq_api_key=os.getenv("GROQ_API_KEY")
)

def review_code(diff):

    prompt = f"""
You are a senior security engineer performing a first-pass security review on a pull request

Analyze the code diff and specifically flag:
- Common security vulnerabilities (OWASP Top 10, SQL injection, XSS, etc.)
- Insecure coding patterns or sensitive data leaks
- Logic flaws that could be exploited
- Performance bottlenecks or critical bugs

Provide actionable feedback in a professional and concise manner.

Code diff:
{diff}
"""
    
    response = llm.invoke(prompt)
    return response.content
