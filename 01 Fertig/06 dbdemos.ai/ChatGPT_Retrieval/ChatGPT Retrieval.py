# Databricks notebook source
# MAGIC %md
# MAGIC
# MAGIC # chatgpt-retrieval
# MAGIC
# MAGIC ## Github-Repository:
# MAGIC
# MAGIC https://github.com/techleadhd/chatgpt-retrieval
# MAGIC
# MAGIC ## Kann lokal auf einem Jupyter Notebook laufen, man braucht kein Databricks für diesen Code
# MAGIC
# MAGIC Simple script to use ChatGPT on your own files.
# MAGIC
# MAGIC Here's the [YouTube Video](https://youtu.be/9AXP7tCI9PI).
# MAGIC
# MAGIC ## Installation
# MAGIC
# MAGIC Install [Langchain](https://github.com/hwchase17/langchain) and other required packages.
# MAGIC ```
# MAGIC pip install langchain openai chromadb tiktoken unstructured
# MAGIC ```
# MAGIC Modify `constants.py.default` to use your own [OpenAI API key](https://platform.openai.com/account/api-keys), and rename it to `constants.py`.
# MAGIC
# MAGIC Place your own data into `data/data.txt`.
# MAGIC
# MAGIC ## Example usage
# MAGIC Test reading `data/data.txt` file.
# MAGIC ```
# MAGIC > python chatgpt.py "what is my dog's name"
# MAGIC Your dog's name is Sunny.
# MAGIC ```
# MAGIC
# MAGIC Test reading `data/cat.pdf` file.
# MAGIC ```
# MAGIC > python chatgpt.py "what is my cat's name"
# MAGIC Your cat's name is Muffy.
# MAGIC ```

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC # Was ist ChatGPT Retrieval?
# MAGIC # 
# MAGIC ## The ChatGPT Retrieval Plugin also allows you to use ChatGPT with a Vector Database 
# MAGIC ## to give it a long-term memory. The plugin also enables ChatGPT to generate responses 
# MAGIC ## based on a company or organizations internal documents and data.
# MAGIC # 
# MAGIC
# MAGIC <div style="text-align: left; line-height: 0; padding-top: 9px;">
# MAGIC   <img src="https://www.antoinebernard.com/content/images/2023/04/main-1.png" alt="ChatGPT_Retrieval" style="width: 600px">
# MAGIC </div>

# COMMAND ----------

pip install langchain openai chromadb tiktoken unstructured

# COMMAND ----------

import os
import sys

import openai
from langchain.chains import ConversationalRetrievalChain, RetrievalQA
from langchain.chat_models import ChatOpenAI
from langchain.document_loaders import DirectoryLoader, TextLoader
from langchain.embeddings import OpenAIEmbeddings
from langchain.indexes import VectorstoreIndexCreator
from langchain.indexes.vectorstore import VectorStoreIndexWrapper
from langchain.llms import OpenAI
from langchain.vectorstores import Chroma

import constants

os.environ["OPENAI_API_KEY"] = constants.APIKEY

# Enable to save to disk & reuse the model (for repeated queries on the same data)
PERSIST = False

query = None
if len(sys.argv) > 1:
  query = sys.argv[1]

if PERSIST and os.path.exists("persist/index"):
  print("Reusing index...\n")
  vectorstore = Chroma(persist_directory="persist", embedding_function=OpenAIEmbeddings())
  index = VectorStoreIndexWrapper(vectorstore=vectorstore)
else:
  #loader = TextLoader("data/data.txt") # Use this line if you only need data.txt
  loader = DirectoryLoader("data/")
  if PERSIST:
    index = VectorstoreIndexCreator(vectorstore_kwargs={"persist_directory":"persist"}).from_loaders([loader])
  else:
    index = VectorstoreIndexCreator().from_loaders([loader])

chain = ConversationalRetrievalChain.from_llm(
  llm=ChatOpenAI(model="gpt-3.5-turbo"),
  retriever=index.vectorstore.as_retriever(search_kwargs={"k": 1}),
)

chat_history = []
while True:
  if not query:
    query = input("Prompt: ")
  if query in ['quit', 'q', 'exit']:
    sys.exit()
  result = chain({"question": query, "chat_history": chat_history})
  print(result['answer'])

  chat_history.append((query, result['answer']))
  query = None


# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC # ChatGPT: Was macht dieser Python Code?
# MAGIC
# MAGIC This Python code is a script for running a Conversational Retrieval Chain powered by the OpenAI GPT-3.5 Turbo model to answer questions based on a given dataset. The code utilizes various modules from the "langchain" library to manage data loading, embeddings, and indexing.
# MAGIC
# MAGIC Here's a breakdown of the code:
# MAGIC
# MAGIC     Import necessary libraries and modules:
# MAGIC         os: For environment variables, including setting the OpenAI API key.
# MAGIC         sys: For system-specific parameters and functions.
# MAGIC         openai: The OpenAI Python library for interacting with GPT-3.5 Turbo.
# MAGIC         Various modules from the "langchain" library.
# MAGIC
# MAGIC     Set the OpenAI API key: The API key is read from a file named constants.py which contains the variable APIKEY.
# MAGIC
# MAGIC     Define a constant PERSIST and set it to False. This flag determines whether to save the model to disk for reuse.
# MAGIC
# MAGIC     Check if there is a command-line argument provided (i.e., sys.argv[1]) and store it in the variable query.
# MAGIC
# MAGIC     If PERSIST is set to True and the index directory already exists (persist/index), then it loads the vectorstore from the saved directory. Otherwise, 
# MAGIC     it creates a new vectorstore index from the data in the "data/" directory.
# MAGIC
# MAGIC     Initialize a ConversationalRetrievalChain with an instantiated GPT-3.5 Turbo model (ChatOpenAI) and a retriever based on the index.
# MAGIC
# MAGIC     Enter a loop to interactively answer questions:
# MAGIC         If query is not provided via a command-line argument, it prompts the user for input.
# MAGIC         If the user enters 'quit', 'q', or 'exit', the script terminates.
# MAGIC         The input query is passed to the ConversationalRetrievalChain.
# MAGIC         The answer from the model is printed.
# MAGIC         The query and the model's answer are added to the chat history.
# MAGIC         The query variable is reset to None to prompt the user for the next question.
# MAGIC
# MAGIC Based on your provided example prompt and input, it seems like the code is trying to answer the question 
# MAGIC "Wie heißt mein Hund?" (What is my dog's name?) and returns "Der Name Ihres Hundes lautet Anja." (The name of your dog is Anja.) 
# MAGIC The user then enters 'q', which causes the script to exit with the SystemExit exception.
# MAGIC
# MAGIC It's worth noting that this code appears to be a snippet of a larger application or script, as some parts are incomplete 
# MAGIC (e.g., missing imports and constants). Additionally, without knowing the complete "langchain" library and its functionalities, 
# MAGIC it's challenging to understand the full context and purpose of this script.
