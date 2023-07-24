# Databricks notebook source
# MAGIC %md
# MAGIC
# MAGIC # Beispiel ChatGPT-Retrieval
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

# DBTITLE 1,Installation der benötigten Python Libraries
pip install langchain openai chromadb tiktoken unstructured

# COMMAND ----------

# DBTITLE 1,Vector Store DB für die angebundenen Dateien erstellen, Conversational Retrieval Chain mit ChatGPT 3.5 Turbo
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
# MAGIC Dieser Python-Code erstellt einen Dialogsystem, der auf maschinellem Lernen und Informationsabruf basiert. 
# MAGIC Es verwendet die OpenAI GPT-3.5-turbo Modell und eine Reihe von Bibliotheken, die anscheinend speziell für
# MAGIC den Bau solcher Systeme erstellt wurden (z. B. langchain, vectorstore, chroma usw.).
# MAGIC
# MAGIC ## Eine allgemeine Übersicht über den Code:
# MAGIC
# MAGIC     Import der notwendigen Bibliotheken und Module: Hier werden verschiedene Bibliotheken importiert, einschließlich openai
# MAGIC     für den Zugriff auf die OpenAI API und verschiedene Module aus der langchain Bibliothek, die für die Erstellung des Dialogsystems benötigt werden.
# MAGIC
# MAGIC     Setzen des OpenAI API-Schlüssels: Der OpenAI API-Schlüssel wird aus einer Konstantendatei geladen und in der Umgebung gesetzt.
# MAGIC
# MAGIC     Abfrageverarbeitung: Der Code überprüft, ob eine Abfrage als Befehlszeilenargument übergeben wurde. Wenn ja, wird diese Abfrage verwendet. 
# MAGIC     Wenn nicht, wird der Benutzer später zur Eingabe einer Abfrage aufgefordert.
# MAGIC
# MAGIC     Wiederverwendung des Index: Der Code überprüft, ob ein vorhandener Index wiederverwendet werden kann. Wenn ja, wird dieser geladen. 
# MAGIC     Wenn nicht, wird ein neuer Index erstellt.
# MAGIC
# MAGIC     Erstellung des Index: Wenn kein bestehender Index wiederverwendet werden kann, wird ein neuer Index erstellt. 
# MAGIC     Dies geschieht durch Laden von Dokumenten aus einem Verzeichnis (oder aus einer einzelnen Datei) und Erstellung eines Index mithilfe eines VectorstoreIndexCreator.
# MAGIC
# MAGIC     Erstellung der Gesprächskette: Eine Gesprächskette (ConversationalRetrievalChain) wird erstellt, die das OpenAI-Modell und den erstellten Index verwendet.
# MAGIC
# MAGIC     Dialogschleife: Schließlich wird eine unendliche Schleife erstellt, in der der Benutzer nach einer Abfrage gefragt wird. 
# MAGIC     Die Abfrage wird dann durch die Gesprächskette verarbeitet und die Antwort wird ausgegeben. Die Abfrage und die Antwort 
# MAGIC     werden auch zur Chat-Historie hinzugefügt, die in zukünftigen Abfragen verwendet wird.
# MAGIC
# MAGIC Bitte beachten Sie, dass ich nicht in der Lage bin, Informationen über die spezifischen langchain, chroma und vectorstore Bibliotheken zu liefern, da diese nicht allgemein bekannt oder dokumentiert sind (bis zu meinem Wissensstand, das bis September 2021 geht). Es könnte sich um spezifische Bibliotheken handeln, die für ein bestimmtes Projekt oder eine bestimmte Organisation entwickelt wurden.
