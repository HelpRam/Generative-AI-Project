import streamlit as st
from langchain_community.llms import Ollama
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Function to load model and get response
def get_ollama_response(question):
    # Initialize the Ollama model
    llm = Ollama(model='llama3')
    # Get the response from the model
    response = llm(question)
    return response

# Initialize our Streamlit app
st.set_page_config(page_title="Q&A")

st.header("Langchain Application")
input_text = st.text_input("Input: ", key="input")

submit = st.button("Ask the question")

# If ask button is clicked
if submit:
    response = get_ollama_response(input_text)
    st.subheader("The Response is")
    st.write(response)
