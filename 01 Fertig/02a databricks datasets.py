# Databricks notebook source
# 55 Sample datasets
display(dbutils.fs.ls('/databricks-datasets'))

# COMMAND ----------

# MAGIC     %sh 
# MAGIC     # Komplette Size in GB, LIEF EWIG, gecancelt!
# MAGIC     du -hc /dbfs/databricks-datasets/power-plant/

# COMMAND ----------

# modificationTime als lesbarer Timestamp

import os
from datetime import datetime
path = '/dbfs/databricks-datasets/airlines'
fdpaths = [path+"/"+fd for fd in os.listdir(path)]
print(" file_path " + " create_date " + " modified_date ")
for fdpath in fdpaths:
  statinfo = os.stat(fdpath)
  create_date = datetime.fromtimestamp(statinfo.st_ctime)
  modified_date = datetime.fromtimestamp(statinfo.st_mtime)
  print(fdpath, create_date, modified_date)


# COMMAND ----------

display(dbutils.fs.ls('/databricks-datasets/amazon/'))

# COMMAND ----------

f = open('/dbfs/databricks-datasets/amazon/README.md', 'r')
#f = open('/dbfs/databricks-datasets/flights/airport-codes-na.txt', 'r')
print(f.read())

# COMMAND ----------

f = open('/dbfs/databricks-datasets/airlines/part-00000', 'r')
print(f.read())

# COMMAND ----------

f = open('/dbfs/databricks-datasets/nyctaxi/readme_nyctaxi.txt', 'r')
print(f.read())

# COMMAND ----------

display(dbutils.fs.ls('/databricks-datasets/nyctaxi/tables/nyctaxi_yellow/'))

# COMMAND ----------

# MAGIC %sql
# MAGIC DESCRIBE DETAIL '/databricks-datasets/nyctaxi/tables/nyctaxi_yellow/'

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE OR REPLACE VIEW nyctaxi_yellow as select * from delta.`/databricks-datasets/nyctaxi/tables/nyctaxi_yellow/`;
# MAGIC
# MAGIC select * from nyctaxi_yellow;

# COMMAND ----------

# MAGIC %sql
# MAGIC select max(pickup_datetime) from nyctaxi_yellow
# MAGIC where pickup_datetime < current_timestamp();

# COMMAND ----------

# MAGIC %sql
# MAGIC describe nyctaxi

# COMMAND ----------

display(dbutils.fs.ls('/databricks-datasets/nyctaxi'))

# COMMAND ----------

# MAGIC     %sh 
# MAGIC     # Komplette Size NYCTAXI in GB
# MAGIC     du -sch /dbfs/databricks-datasets/nyctaxi/

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC ## Parquet-Dateien laden in eigenen Mount-Point (ADLS Gen2)
# MAGIC ## <a href="https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page">https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page</a>

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE OR REPLACE VIEW nyctaxi_yellow_parquet as select * from parquet.`/mnt/deltalake/yellow_taxi_parquet/`;
# MAGIC
# MAGIC select * from nyctaxi_yellow_parquet;

# COMMAND ----------

# MAGIC %sql
# MAGIC describe nyctaxi_yellow_parquet
