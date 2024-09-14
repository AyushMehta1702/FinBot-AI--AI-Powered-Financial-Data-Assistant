import streamlit as st
import pandas as pd
from sqlalchemy import create_engine
from langchain_community.utilities import SQLDatabase
from langchain_experimental.sql import SQLDatabaseChain
from langchain_community.chat_models import ChatOpenAI
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain import LLMChain

import os

from dotenv import load_dotenv
load_dotenv()



# Setup the OpenAI API key
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

# Initialize the OpenAI LLM
openai_llm = OpenAI(model_name="gpt-4o-mini", openai_api_key=OPENAI_API_KEY)
llm = ChatOpenAI(temperature=0)

# Initialize the SQL Database wrapper
engine = create_engine('postgresql+psycopg2://postgres:001127@localhost:5432/F_Bot_DB')
db = SQLDatabase(engine)
db_url = 'postgresql+psycopg2://postgres:001127@localhost:5432/F_Bot_DB'

# Define the prompt template
prompt_template = """
You are an expert in financial data. Given the following SQL query:

{query}

Please write a brief, accurate, and helpful answer based on the financial data provided.
"""

prompt = PromptTemplate(input_variables=["query"], template=prompt_template)

# Create a LangChain SQL database chain
sql_chain = SQLDatabaseChain(llm=openai_llm, database=db, prompt=prompt)

# # Streamlit App Configuration
# st.set_page_config(page_title="Finance Chatbot", page_icon="💬", layout="centered")
#
# st.title("💬 Finance Data Chatbot")
#
# # Initialize session state to store chat history
# if "messages" not in st.session_state:
#     st.session_state.messages = []
#
# # Function to get the response from the model
# def get_response(query):
#     try:
#         # Use the SQL chain to get the result
#         response = sql_chain.run(query)
#         return response
#     except Exception as e:
#         return f"Error: {str(e)}"
#
# # Display the chat messages
# for message in st.session_state.messages:
#     st.write(f"**{message['role'].capitalize()}:** {message['content']}")
#
# # User input
# user_input = st.text_input("You:", "", key="input")
#
# if st.button("Send"):
#     if user_input:
#         # Add the user's message to the chat history
#         st.session_state.messages.append({"role": "user", "content": user_input})
#
#         # Get the response from the model
#         response = get_response(user_input)
#
#         # Add the model's response to the chat history
#         st.session_state.messages.append({"role": "bot", "content": response})
#
#         # Clear the input box
#         st.text_input("You:", "", key="input", value="")

