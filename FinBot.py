import streamlit as st
from langchain_community.utilities import SQLDatabase
from langchain_experimental.sql import SQLDatabaseChain
from langchain_community.chat_models import ChatOpenAI
from chat_ui02 import chat_interface
from UI01 import chat_interface
import os
from dotenv import load_dotenv
load_dotenv()

# Setup the OpenAI API key
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

# Initialize the OpenAI LLM
llm = ChatOpenAI(temperature=0.7, openai_api_key=OPENAI_API_KEY)

# Initialize the SQL Database wrapper
DB = os.getenv('DataBase')
database = SQLDatabase.from_uri(DB)


def initialize_sql_chain():
    sql_chain = SQLDatabaseChain.from_llm(llm=llm, db=database)
    return sql_chain


sql_chain = initialize_sql_chain()

chat_interface(sql_chain)

# # streamlit Setup
# st.title("Finance Bot")
#
# st.write("Connected to the database. You can now ask questions about the financial data!")
#
# query = st.text_input("Enter your question:")
#
# if query:
#     try:
#         sql_query = sql_chain.run(query)
#
#         st.write(f"**Answer:** {sql_query}")
#     except Exception as e:
#         st.error(f"An error occurred: {str(e)}")
#         st.write("Debugging info:")
#         st.write(f"Query: {query}")
#         st.write(f"Type of query: {type(query)}")
#         st.write("Ensure that `sql_chain.run()` is correctly handling the input.")
