# Databricks notebook source
# MAGIC %md
# MAGIC <div style="text-align: left; line-height: 0; padding-top: 9px;">
# MAGIC   <img src="https://i.ibb.co/4S3DCY2/Schema-Evolution.jpg" alt="Delta ist parquet, aber besser" style="width: 600px">
# MAGIC </div>

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC # 1. SET spark.databricks.delta.schema.autoMerge.enabled = true

# COMMAND ----------

spark.sql("SET spark.databricks.delta.schema.autoMerge.enabled = true")

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC # 2. Describe flights_delta

# COMMAND ----------

# MAGIC %sql
# MAGIC Describe flights_delta

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC # 3. Merge mit Dummy-Insert

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC MERGE INTO flights_delta                                          t
# MAGIC USING      (SELECT 'ATL' AS Origin, 'Hello world' AS NEW_COLUMN)  s
# MAGIC ON                   1 = 2
# MAGIC WHEN MATCHED
# MAGIC   THEN UPDATE SET *
# MAGIC WHEN NOT MATCHED
# MAGIC   THEN INSERT *

# COMMAND ----------

# MAGIC %sql
# MAGIC Describe flights_delta

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC select * from flights_delta where NEW_COLUMN IS NOT NULL

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC # 4. Time Travel für Time Series Analytics

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC SELECT count(*) - 
# MAGIC (   SELECT count(*)
# MAGIC     FROM flights_delta VERSION AS OF 1 WHERE ORIGIN = 'ATL') AS ATL_COUNT_INSERTS
# MAGIC FROM flights_delta
# MAGIC WHERE ORIGIN = 'ATL'
