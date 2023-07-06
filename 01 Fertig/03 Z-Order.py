# Databricks notebook source
# MAGIC %md
# MAGIC
# MAGIC # Delta Tables: Optimize + Z-Order explained
# MAGIC # 
# MAGIC
# MAGIC <div style="text-align: left; line-height: 0; padding-top: 9px;">
# MAGIC   <img src="https://i.ibb.co/dBg2ZWd/Z-Order-1.jpg" alt="Z-Order 1" style="width: 600px">
# MAGIC </div>

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC <div style="text-align: left; line-height: 0; padding-top: 9px;">
# MAGIC   <img src="https://i.ibb.co/HNP3nxF/Z-Order-2.jpg" alt="Z-Order 2" style="width: 600px">
# MAGIC </div>

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC # 1. Read flight data

# COMMAND ----------

# Verzeichnis löschen
# dbutils.fs.rm("/tmp/flights_delta", recurse=True)

# COMMAND ----------

display(dbutils.fs.ls('/databricks-datasets/asa/airlines/2008.csv'))

# COMMAND ----------

# MAGIC %sh
# MAGIC du -h /dbfs/databricks-datasets/asa/airlines/2008.csv

# COMMAND ----------

flights_csv = spark.read.format("csv") \
    .option("header", "true") \
    .option("inferschema", "true") \
    .load("/databricks-datasets/asa/airlines/2008.csv")

# COMMAND ----------

display(flights_csv)

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC # 2. Write to Parquet

# COMMAND ----------

    flights_csv.write.format("parquet") \
    .mode("overwrite") \
    .partitionBy("Origin") \
    .save("/tmp/flights_parquet")

# COMMAND ----------

# MAGIC %md
# MAGIC ## Anzahl Parquet-Dateien

# COMMAND ----------

# MAGIC %sh
# MAGIC cd /dbfs/tmp/flights_parquet/
# MAGIC find . -name '*.parquet' | wc -l

# COMMAND ----------

# MAGIC     %sh du -h /dbfs/tmp/flights_parquet/

# COMMAND ----------

display(dbutils.fs.ls('/tmp/flights_parquet/Origin=ATL/'))

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC # 3. Test the performance of the parquet-based table, we will query the top 20 airlines with most flights in 2008 on Mondays by month

# COMMAND ----------

from pyspark.sql.functions import count

flights_parquet = spark.read.format("parquet") \
.load("/tmp/flights_parquet")
display(flights_parquet.filter("DayOfWeek = 1") \
.groupBy("Month", "Origin") \
.agg(count("*").alias("TotalFlights")) \
.orderBy("TotalFlights", ascending=False) \
.limit(20)
)

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC # 4. Abfrage lief über 30 Sek., now, let’s try Delta

# COMMAND ----------

    flights_parquet.write.format("delta") \
    .mode("overwrite") \
    .partitionBy("Origin") \
    .save("/tmp/flights_delta")

    # Create delta table
    display(spark.sql("DROP TABLE IF EXISTS flights_delta"))
    display(spark.sql("CREATE TABLE flights_delta USING DELTA LOCATION '/tmp/flights_delta'"))

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC # 5. Optimize + Z-Order nach Spalte DayOfWeek

# COMMAND ----------

display(spark.sql("OPTIMIZE flights_delta ZORDER BY (DayofWeek)"))

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC ## Anzahl Parquet-Dateien in Delta Table

# COMMAND ----------

# MAGIC %sh
# MAGIC cd /dbfs/tmp/flights_delta/
# MAGIC find . -name '*.parquet' | wc -l

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC # 6. Gleiche Abfrage auf Delta in 6 Sek., 5x so schnell

# COMMAND ----------

    flights_delta_read = spark.read \
    .format("delta") \
    .load("/tmp/flights_delta")

    display(
    flights_delta_read \
    .filter("DayOfWeek = 1") \
    .groupBy("Month","Origin") \
    .agg(count("*") \
    .alias("TotalFlights")) \
    .orderBy("TotalFlights", ascending=False) \
    .limit(20)
    )

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC # 7. DESCRIBE HISTORY

# COMMAND ----------

display(spark.sql("DESCRIBE HISTORY flights_delta"))

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC # 8. Time Travel: Version 0 (also ohne Optimize + Z-Order)

# COMMAND ----------

    flights_delta_version_0 = spark.read \
    .format("delta") \
    .option("versionAsOf", "0") \
    .load("/tmp/flights_delta")

    display(
    flights_delta_version_0.filter("DayOfWeek = 1") \
    .groupBy("Month","Origin") \
    .agg(count("*") \
    .alias("TotalFlights")) \
    .orderBy("TotalFlights", ascending=False) \
    .limit(20)
    )

# COMMAND ----------

display(dbutils.fs.ls('/tmp/flights_delta/'))

# COMMAND ----------

display(dbutils.fs.ls('/tmp/flights_delta/Origin=ATL/'))

# COMMAND ----------

f = open('/dbfs/tmp/flights_delta/_delta_log/00000000000000000001.json', 'r')
print(f.read())

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC # 9. COUNT(*)

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC select count(*), min(origin), max(origin) from flights_delta;

# COMMAND ----------

# MAGIC %sh du -h /dbfs/tmp/flights_delta/

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC # 10. DROP TABLE (External, unmanaged table)
# MAGIC
# MAGIC Even though we can delete tables in the background without affecting workloads, it is always good to make sure that we run DELETE FROM and VACUUM before drop command on any table. This ensures that the metadata and file sizes are cleaned up before initiating the actual data deletion.
# MAGIC
# MAGIC For example, if we are trying to delete the Delta table “emptbl”, run the following commands before starting the DROP TABLE command:
# MAGIC
# MAGIC 1. Run DELETE FROM: DELETE FROM emptbl
# MAGIC
# MAGIC 2. Run VACUUM with an interval of zero: VACUUM emptbl RETAIN 0 HOURS
# MAGIC
# MAGIC 3. DROP TABLE emptbl

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC --DELETE FROM flights_delta;

# COMMAND ----------

# spark.sql("SET spark.databricks.delta.retentionDurationCheck.enabled = false")

# COMMAND ----------

# MAGIC %sql
# MAGIC --VACUUM flights_delta RETAIN 0 HOURS;
# MAGIC
# MAGIC --DROP TABLE flights_delta;

# COMMAND ----------

# Verzeichnis löschen
#dbutils.fs.rm("/tmp/flights_delta", recurse=True)
