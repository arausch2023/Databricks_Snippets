# Databricks notebook source
# MAGIC %md
# MAGIC
# MAGIC https://www.dbdemos.ai/demo.html?demoName=llm-dolly-chatbot
# MAGIC
# MAGIC <div style="text-align: left; line-height: 0; padding-top: 9px;">
# MAGIC   <img src="https://raw.githubusercontent.com/databricks-demos/dbdemos-resources/main/images/product/llm-dolly/llm-dolly-full.png" alt="LLM Dolly Chatbot" style="width: 600px">
# MAGIC </div>

# COMMAND ----------

# MAGIC %pip install dbdemos 

# COMMAND ----------

import dbdemos
dbdemos.help()
dbdemos.list_demos()

# COMMAND ----------

# MAGIC %md 
# MAGIC
# MAGIC # HINWEIS: Cluster-Size
# MAGIC
# MAGIC # Bitte erstellt einen Single-Node ML-Cluster mit Standard_DS4_v2 
# MAGIC # (28 GB Memory, 8 Cores, 13.1.x-cpu-ml-scala2.12), ihr braucht 
# MAGIC # > 20 GB RAM für das LLM-Modell (pytorch mit 7 Mrd. Textbausteinen = 13,0 GB)
# MAGIC #  
# MAGIC
# MAGIC <div style="text-align: left; line-height: 0; padding-top: 9px;">
# MAGIC   <img src="https://i.ibb.co/s5Tk5r5/ML-Standard-DS4-Cluster.jpg" alt="ML-Standard-DS4-Cluster" style="width: 600px">
# MAGIC </div>

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC # Ich erhielt folgenden Fehler:
# MAGIC
# MAGIC <div style="text-align: left; line-height: 0; padding-top: 9px;">
# MAGIC   <img src="https://i.ibb.co/b3N7BSn/Fehler-Dolly-ML-Cluster.jpg" alt="Fehler Dolly ML-Cluster" style="width: 600px">
# MAGIC </div>

# COMMAND ----------

dbdemos.install('llm-dolly-chatbot', path='./', overwrite = True)
