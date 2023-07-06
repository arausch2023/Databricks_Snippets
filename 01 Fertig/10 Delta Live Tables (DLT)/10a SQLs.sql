-- Databricks notebook source
select count(*) from demos_dlt_cdc_arausch.scd2_customers;

-- COMMAND ----------

select * from demos_dlt_cdc_arausch.customers_cdc_clean
order by operation_date desc;

-- COMMAND ----------

select * from demos_dlt_cdc_arausch.customers_cdc
order by operation_date desc;
