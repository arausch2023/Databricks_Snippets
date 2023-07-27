# Databricks notebook source
# MAGIC %md
# MAGIC
# MAGIC # Secret Scopes für Verwaltung der persönlichen Zugangsinformationen wie API Keys
# MAGIC
# MAGIC https://learn.microsoft.com/en-us/azure/databricks/security/secrets/secret-scopes
# MAGIC
# MAGIC https://www.youtube.com/watch?v=HZ00AznWvKc

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC Dazu muss die Databricks CLI genutzt werden, Installations-Dateien: https://github.com/databricks/cli/releases
# MAGIC
# MAGIC ## Befehle:
# MAGIC D:\Databricks\databricks_cli_0.200.2_windows_amd64\databricks configure
# MAGIC
# MAGIC Hier dann die URL von eurem Databricks-Workspace eintragen, Bsp.: "adb-3456974533129641.1.azuredatabricks.net"
# MAGIC Ihr braucht noch einen Personal Access Token, findet ihr unter User Settings -> Access Tokens
# MAGIC
# MAGIC D:\Databricks\databricks_cli_0.200.2_windows_amd64\databricks secrets create-scope openai_key_secret_scope
# MAGIC
# MAGIC Hier dann als string-value z. Bsp. euren OpenAI API Key hinterlegen
# MAGIC
# MAGIC D:\Databricks\databricks_cli_0.200.2_windows_amd64\databricks secrets put-secret openai_key_secret_scope openai_key_secret_key --string-value sk-**Hier euer OpenAI API Key ohne " oder '**
# MAGIC
# MAGIC D:\Databricks\databricks_cli_0.200.2_windows_amd64\databricks secrets list-scopes
# MAGIC
# MAGIC Oder für Mounten eines Azure Data Lake Storage Gen2 könnt ihr als Secret Scope eure Azure SubscriptionID hinterlegen, also immer dann wenn
# MAGIC man nicht hardcodiert Zugangsdaten im Python-Code haben will Secret Scope verwenden.

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC # Secret Scope für Azure Key Vault

# COMMAND ----------

# MAGIC %md 
# MAGIC
# MAGIC ## Von eurem Workspace die URL nehmen, Bsp.:
# MAGIC ## https://[databricks-instance]#secrets/createScope
# MAGIC
# MAGIC ### Bsp.: https://adb-3456974533129641.1.azuredatabricks.net#secrets/createScope

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC <div style="text-align: left; line-height: 0; padding-top: 9px;">
# MAGIC   <img src="https://learn.microsoft.com/en-us/azure/databricks/_static/images/secrets/azure-kv-scope.png" alt="Secret Scope" style="width: 600px">
# MAGIC </div>

# COMMAND ----------

# DBTITLE 1,Secret Scope anschauen
mysecret = dbutils.secrets.get("openai_key_secret_scope", "openai_key_secret_key")

for i in mysecret:
    print(i)

# COMMAND ----------

# MAGIC %sql
# MAGIC SHOW GROUPS
