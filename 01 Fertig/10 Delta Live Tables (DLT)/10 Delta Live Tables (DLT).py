# Databricks notebook source
# MAGIC %md
# MAGIC
# MAGIC # Delta Live Tables (DLT)
# MAGIC
# MAGIC ## Heute schauen wir uns die Erweiterung der Delta Tables an, nämlich Delta **Live** Tables.
# MAGIC ## Wir gehen eine Demo durch, wo wir  Delta Live Tables verwenden und
# MAGIC ## in einem Workflow mit Pipelines komplett von Quelle -> Dashboard die Aktualisierung durchführen.

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC ## Um Delta Live Tables zu verstehen müssen wir noch einen Blick auf die 
# MAGIC ## Grund-Architektur eines Delta Lakes schauen, nämlich die Multi-Hop Medaillon-Architektur:
# MAGIC
# MAGIC ## 
# MAGIC
# MAGIC <div style="text-align: left; line-height: 0; padding-top: 9px;">
# MAGIC   <img src="https://i.ibb.co/J2mNS4N/Medaillon.jpg" alt="Medaillon" style="width: 600px">
# MAGIC </div>

# COMMAND ----------

# MAGIC %md
# MAGIC <div style="text-align: left; line-height: 0; padding-top: 9px;">
# MAGIC   <img src="https://i.ibb.co/fD66h3K/Delta-Live-Tables.jpg" alt="Delta Live Tables" style="width: 600px">
# MAGIC </div>

# COMMAND ----------

# MAGIC %md 
# MAGIC
# MAGIC # dbdemos.ai Demo: CDC pipeline with Delta Live Table
# MAGIC
# MAGIC https://www.dbdemos.ai/demo.html?demoName=dlt-cdc
# MAGIC
# MAGIC Ingest Change Data Capture flow with APPLY INTO and simplify SCDT2 implementation.
# MAGIC
# MAGIC This demo highlight how Delta Live Table simplify CDC (Change Data Capture).
# MAGIC CDC is typically done ingesting changes from external system (ERP, SQL databases) with tools like fivetran, debezium etc.
# MAGIC In this demo, we'll show you how to re-create your table consuming CDC information.
# MAGIC We'll also implement a SCD2 (Slowly Changing Dimention table of type 2). While this can be really tricky to implement when data arrives out of order, DLT makes this super simple with one simple keyword.
# MAGIC
# MAGIC Ultimately, we'll show you how to programatically scan multiple incoming folder and trigger N stream (1 for each CDC table), leveraging DLT with python.
# MAGIC
# MAGIC <div style="text-align: left; line-height: 0; padding-top: 9px;">
# MAGIC   <img src="https://www.dbdemos.ai/assets/img/dbdemos/dlt-cdc-dlt-0.png" alt="Delta Live Tables Demo" style="width: 600px">
# MAGIC </div>

# COMMAND ----------

# MAGIC %pip install dbdemos

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC # dbdemos.install erstellt einen Unterordner "/dlt-cdc/" mit allen Notebooks der Demo

# COMMAND ----------

import dbdemos
dbdemos.install('dlt-cdc')
