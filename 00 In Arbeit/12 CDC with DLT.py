# Databricks notebook source
# MAGIC %md
# MAGIC
# MAGIC https://www.youtube.com/watch?v=L-dCMdME_fw&t=10s
# MAGIC
# MAGIC https://docs.databricks.com/delta-live-tables/cdc.html

# COMMAND ----------

-- Create and populate the target table.
CREATE OR REFRESH STREAMING TABLE target;

APPLY CHANGES INTO
  live.target
FROM
  stream(cdc_data.users)
KEYS
  (userId)
APPLY AS DELETE WHEN
  operation = "DELETE"
APPLY AS TRUNCATE WHEN
  operation = "TRUNCATE"
SEQUENCE BY
  sequenceNum
COLUMNS * EXCEPT
  (operation, sequenceNum)
STORED AS
  SCD TYPE 1;

