# Databricks notebook source
# MAGIC %md
# MAGIC
# MAGIC # AI Functions: query LLM with DBSQL
# MAGIC
# MAGIC https://www.dbdemos.ai/demo.html?demoName=sql-ai-functions
# MAGIC

# COMMAND ----------

# MAGIC %pip install dbdemos 

# COMMAND ----------

import dbdemos
dbdemos.list_demos()

# COMMAND ----------

import dbdemos
dbdemos.install('sql-ai-functions', path='./', overwrite = True)
