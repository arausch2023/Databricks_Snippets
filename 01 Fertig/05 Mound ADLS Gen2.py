# Databricks notebook source
# MAGIC %md
# MAGIC
# MAGIC # Mount ADLS Gen2
# MAGIC
# MAGIC ## ADLS Gen2 sollte "Enable hierarchical namespace" aktiviert haben
# MAGIC
# MAGIC ### [container]    = Container-Name
# MAGIC ### [storage-name] = Storage-Name
# MAGIC ### [Account Key] = Access Key

# COMMAND ----------

dbutils.fs.mount(
   source = 'wasbs://[container]@[storage-name].blob.core.windows.net/',
   mount_point = '[Relative path to mount point]]',
   extra_configs = {'fs.azure.account.key.[storage-name].blob.core.windows.net':'[Account Key]'}
)

# COMMAND ----------

dbutils.fs.mount(
   source = 'wasbs://deltalake@sbxarauschsa.blob.core.windows.net/',
   mount_point = '/mnt/deltalake',
   extra_configs = {'fs.azure.account.key.sbxarauschsa.blob.core.windows.net':'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'}
)

# COMMAND ----------

dbutils.fs.ls('/mnt/deltalake')

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC # Azure Storage Explorer
# MAGIC
# MAGIC https://azure.microsoft.com/en-us/products/storage/storage-explorer
# MAGIC
# MAGIC <div style="text-align: left; line-height: 0; padding-top: 9px;">
# MAGIC   <img src="https://cdn-dynmedia-1.microsoft.com/is/image/microsoftcorp/value-prop?resMode=sharp2&op_usm=1.5,0.65,15,0&wid=847&qlt=100&fmt=png-alpha&fit=constrain" alt="Azure Storage Explorer" style="width: 600px">
# MAGIC </div>

# COMMAND ----------

flights_csv = spark.read.format("csv") \
    .option("header", "true") \
    .option("inferschema", "true") \
    .load("/databricks-datasets/asa/airlines/2008.csv")

# COMMAND ----------

    flights_csv.write.format("parquet") \
    .mode("overwrite") \
    .partitionBy("Origin") \
    .save("/mnt/deltalake/flights_parquet")

# COMMAND ----------

(dbutils.fs.ls('/mnt/deltalake/flights_parquet/Origin=ABE/'))

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC # Unmount

# COMMAND ----------

dbutils.fs.unmount('/mnt/deltalake')

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC ## Bsp. Zugriff auf CSV auf ADSL Gen2-Mount

# COMMAND ----------

infomotion_csv = spark.read.format("csv") \
    .option("header", "true") \
    .option("inferschema", "true") \
    .load("/dbfs/mnt/deltalake/infomotion.csv")

# COMMAND ----------

f = open('/dbfs/mnt/deltalake/infomotion.csv', 'r')
print(f.read())
