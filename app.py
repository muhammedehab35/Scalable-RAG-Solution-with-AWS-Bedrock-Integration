import json
import os 
import sys
import boto3
import streamlit as st


from langchain_community.embeddings import BedrockEmbeddings
# from langchain.llms.bedrock import Bedrock
from langchain_community.llms import Bedrock
from langchain.prompts import PromptTemplate
from langchain.chains import RetrievalQA
# from langchain.vectorstores import FAISS
from langchain_community.vectorstores import FAISS
from QASystem.ingestion import data_ingestion,get_vector_store
from QASystem.retrievalandgeneration import get_llama2_llm,get_response_llm

bedrock=boto3.client(service_name="bedrock-runtime")
bedrock_embeddings=BedrockEmbeddings(model_id="amazon.titan-embed-text-v1",client=bedrock)

def main():
    # Setting page title and favicon
    st.set_page_config(page_title="QA with Doc", page_icon=":memo:")

    # Main header
    st.title("Chat with Llama-bot about your doc")
    st.markdown("*Powered by AWSBedrock and Langchain*")

    # User input text box
    user_question = st.text_input("Ask something about the input PDF doc")

    # Button to ask llama model
    if st.button("Ask Llama Model"):
        with st.spinner("Fetching response from VectorDB..."):
            faiss_index = FAISS.load_local("faiss_index", bedrock_embeddings, allow_dangerous_deserialization=True)
            llm = get_llama2_llm()

            # Function to get response from llama model
            response = get_response_llm(llm, faiss_index, user_question)
            st.write(response)
            st.success("Done")

    # Sidebar for updating vector store
    with st.sidebar:
        st.title("Update or Create Vector Store")
        if st.button("Update VectorDB"):
            with st.spinner("Updating the vector database with the updated doc in backend..."):
                # Update vector database function
                docs = data_ingestion()
                get_vector_store(docs)
                st.success("VectorDB updated successfully!")
                
if __name__=="__main__":
    #this is my main method
    main()