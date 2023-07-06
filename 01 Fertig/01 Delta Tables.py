# Databricks notebook source
# MAGIC %md
# MAGIC
# MAGIC <div style="text-align: left; line-height: 0; padding-top: 9px;">
# MAGIC   <img src="https://camo.githubusercontent.com/5535944a613e60c9be4d3a96e3d9bd34e5aba5cddc1aa6c6153123a958698289/68747470733a2f2f646f63732e64656c74612e696f2f6c61746573742f5f7374617469632f64656c74612d6c616b652d77686974652e706e67" alt="Delta Lake" style="width: 600px">
# MAGIC </div>
# MAGIC
# MAGIC # Was ist ein Delta Lake? Was sind Delta Tables?
# MAGIC
# MAGIC <b>Open-source storage framework mit einem dateibasierten Transaktionsprotokoll</b> (Parquet-Dateien mit dateibasiertem Transaction-Log als JSON-Dateien) mit ACID-Funktionalität.
# MAGIC
# MAGIC # ACID:
# MAGIC
# MAGIC <div style="text-align: left; line-height: 0; padding-top: 9px;">
# MAGIC   <img src="https://s7280.pcdn.co/wp-content/uploads/2020/04/acid-data.png" alt="ACID" style="width: 600px">
# MAGIC </div>
# MAGIC
# MAGIC # Delta Lake Historie:
# MAGIC
# MAGIC <div style="text-align: left; line-height: 0; padding-top: 9px;">
# MAGIC   <img src="https://i.ibb.co/FhbQs9d/Delta-Lake-Historie.jpg" alt="Delta Lake Historie:" style="width: 600px">
# MAGIC </div>

# COMMAND ----------

# MAGIC %md
# MAGIC <div style="text-align: left; line-height: 0; padding-top: 9px;">
# MAGIC   <img src="https://i.ibb.co/4NdL9HM/csv-Parquet.jpg" alt="csv->Parquet" style="width: 600px">
# MAGIC </div>

# COMMAND ----------

# MAGIC %md
# MAGIC <div style="text-align: left; line-height: 0; padding-top: 9px;">
# MAGIC   <img src="https://i.ibb.co/x6zRCMN/Delta-ist-Parquet-1.jpg" alt="Delta ist parquet, aber besser" style="width: 600px">
# MAGIC </div>

# COMMAND ----------

# MAGIC %md
# MAGIC <div style="text-align: left; line-height: 0; padding-top: 9px;">
# MAGIC   <img src="https://i.ibb.co/1XvpdWn/Delta-ist-Parquet-2.jpg" alt="Delta ist parquet, aber besser" style="width: 600px">
# MAGIC </div>

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC # Weitere Funktionalitäten von Delta gegenüber Parquet:
# MAGIC
# MAGIC - <b>Schema-Evolution</b> nun möglich in Databricks für Delta (neue Spalte hinzufügen per Merge)
# MAGIC - <b>Time Travel</b> bzw. Restore (select * from table VERSION AS OF 3)
# MAGIC - <b>Optimize</b> (Komprimieren kleinerer Parquet-Teildateien in größere, besser komprimierte Teildateien; ursprüngliche Parquet-Teildateien bleiben erhalten) 
# MAGIC - <b>Z-Order</b> (sortiere die Daten nach Spalten vor dem Schreiben, optimiert Data Skipping)
# MAGIC - <b>Vacuum</b> (entfernt ältere Versionen, House-Keeping)

# COMMAND ----------

# MAGIC %md
# MAGIC # Community Delta Lake 
# MAGIC
# MAGIC ## <a href="https://delta.io/">https://delta.io/</a>
