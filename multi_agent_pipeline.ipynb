# ============================
# پروژه: سیستم چندعامله با LangChain
# ============================

from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# ============================
# 1. بارگذاری مدل
# ============================
llm = ChatOllama(model="llama3.2")

# ============================
# 2. تعریف عامل‌ها
# ============================
def researcher_agent(topic):
    prompt = ChatPromptTemplate.from_template(
        "You are a researcher. Find accurate and relevant information about: {topic}"
    )
    chain = prompt | llm | StrOutputParser()
    return chain.invoke({"topic": topic})

def analyst_agent(research):
    prompt = ChatPromptTemplate.from_template(
        "You are an analyst. Analyze this information and extract key insights:\n{research}"
    )
    chain = prompt | llm | StrOutputParser()
    return chain.invoke({"research": research})

def writer_agent(analysis):
    prompt = ChatPromptTemplate.from_template(
        "You are a writer. Write a clear and concise summary based on this analysis:\n{analysis}"
    )
    chain = prompt | llm | StrOutputParser()
    return chain.invoke({"analysis": analysis})

# ============================
# 3. اجرا
# ============================
topic = "Applications of AI in healthcare"

print("=== Researcher ===")
research = researcher_agent(topic)
print(research[:500])

print("\n=== Analyst ===")
analysis = analyst_agent(research)
print(analysis[:500])

print("\n=== Writer ===")
summary = writer_agent(analysis)
print(summary)