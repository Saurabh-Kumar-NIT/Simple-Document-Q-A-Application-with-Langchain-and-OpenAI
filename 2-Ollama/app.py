!pip install -U langchain langchain-openai

LANGSMITH_TRACING=true
LANGSMITH_ENDPOINT="https://api.smith.langchain.com"
LANGSMITH_API_KEY="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"
LANGSMITH_PROJECT="pr-frosty-gunpowder-60"
OPENAI_API_KEY="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"

from langchain_openai import ChatOpenAI

llm = ChatOpenAI()
llm.invoke("Hello, world!")

#import os 
#from dotenv import load_dotenv


#from langchain_community.llms import Ollama
#import streamlit as st
#from langchain_core.prompts import ChatPromptTemplate
#from langchain_core.output_parsers import StrOutputParser

#load_dotenv()

# Langsmith tracking
#os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
#os.environ["LANGCHAIN_TRACKING_V2"] = 'true'
#os.environ["LANGCHAIN_PROJECT"] = os.getenv("LANGCHAIN_PROJECT")


## Prompt template
#prompt = ChatPromptTemplate.from_messages(
#    [
#        ("system","You are a helpful assistant. Please respond to the question asked"),
#        ("user","Question:{question}")
#    ]
#)


## Streamlit framework
#st.title("Langchain Demo with gemma model")
#input_text = st.text_input("What question you have in mind")


## Ollama and gemma model
llm = Ollama(model="gemma:2b")
output_parser=StrOutputParser()
chain = prompt | llm | output_parser

if input_text:
    st.write(chain.invoke({"question":input_text}))







