from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
# from langchain_community.vectorstores import FAISS
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import BedrockEmbeddings
# from langchain.llms.bedrock import Bedrock
from langchain_community.llms import Bedrock

import json
import os
import sys
import boto3


## bedrock client
bedrock=boto3.client(service_name="bedrock-runtime")
bedrock_embeddings=BedrockEmbeddings(model_id="amazon.titan-embed-text-v1",client=bedrock)
# You need to place access request for "Titan Embeddings G1 - Text" 
# from "Model Access" section of AWS Bedrock page for above model_id


def data_ingestion():
    loader=PyPDFDirectoryLoader("./data")
    documents=loader.load()
    
    
    text_splitter=RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=1000)
    text_splitter.split_documents(documents)
    
    docs=text_splitter.split_documents(documents)
    
    return docs


def get_vector_store(docs):
    vector_store_faiss=FAISS.from_documents(docs,bedrock_embeddings)
    vector_store_faiss.save_local("faiss_index")
    return vector_store_faiss
    
if __name__ == '__main__':
    docs=data_ingestion()
    get_vector_store(docs)


# Run: python C:/Users/Personal/Desktop/DSMP2023-2024/Self_Researched_Projects/Proj-14/RAG-Application-AWS/QASystem/ingestion.py
# i.e python <path of ingestion.py file in forward slash format> from your terminal to generate faiss_index directory in local
# where your data embedding gets stored.
    
# (FYI, while running this file, it might show some warning in the terminal but that's ok)