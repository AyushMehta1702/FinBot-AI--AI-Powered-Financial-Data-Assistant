import streamlit as st
from langchain_community.utilities import SQLDatabase
from langchain_experimental.sql import SQLDatabaseChain
# from langchain_community.chat_models import ChatOpenAI
from langchain_openai import ChatOpenAI

from Chatbot_UI import chat_interface
import os
from dotenv import load_dotenv
load_dotenv()

# Setup the OpenAI API key
api_key = st.secrets["OPENAI_API_KEY"]
DB = st.secrets["DataBase"]
# Initialize the OpenAI LLM
llm = ChatOpenAI(temperature=0.7, openai_api_key=api_key)

# Initialize the SQL Database wrapper
#DB = os.getenv('DataBase')

database = SQLDatabase.from_uri(DB)


def initialize_sql_chain():
    sql_chain = SQLDatabaseChain.from_llm(llm=llm, db=database)
    return sql_chain


sql_chain = initialize_sql_chain()

chat_interface(sql_chain)