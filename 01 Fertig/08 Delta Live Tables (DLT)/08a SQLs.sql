-- Databricks notebook source
select count(*) from demos_dlt_cdc_arausch.scd2_customers;

-- COMMAND ----------

select * from demos_dlt_cdc_arausch.scd2_customers
where id = '6d2b2de6-92a2-40ec-93a4-810a105e7847';

