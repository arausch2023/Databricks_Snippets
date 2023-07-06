# Databricks notebook source
# MAGIC %md
# MAGIC
# MAGIC https://www.dbdemos.ai/#explore_dbdemos

# COMMAND ----------

# MAGIC %pip install dbdemos

# COMMAND ----------

import dbdemos
dbdemos.help()
dbdemos.list_demos()

# COMMAND ----------

dbdemos.install('llm-dolly-chatbot')
