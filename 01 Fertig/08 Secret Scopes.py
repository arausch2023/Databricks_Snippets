# Databricks notebook source
# MAGIC %md
# MAGIC
# MAGIC # Secret Scopes für Verwaltung der persönlichen Zugangsinformationen wie API Keys
# MAGIC
# MAGIC https://www.youtube.com/watch?v=HZ00AznWvKc
# MAGIC
# MAGIC

# COMMAND ----------

Dazu muss die Databricks CLI genutzt werden, Installations-Dateien: https://github.com/databricks/cli/releases

## Befehle:
D:\Databricks\databricks_cli_0.200.2_windows_amd64\databricks configure

Hier dann die URL von eurem Databricks-Workspace eintragen, Bsp.: "adb-3456974533129641.1.azuredatabricks.net"
Ihr braucht noch einen Personal Access Token, findet ihr unter User Settings -> Access Tokens

D:\Databricks\databricks_cli_0.200.2_windows_amd64\databricks secrets create-scope openai_key_secret_scope

Hier dann als string-value z. Bsp. euren OpenAI API Key hinterlegen

D:\Databricks\databricks_cli_0.200.2_windows_amd64\databricks secrets put-secret openai_key_secret_scope openai_key_secret_key --string-value sk-**Hier euer OpenAI API Key ohne " oder '**

D:\Databricks\databricks_cli_0.200.2_windows_amd64\databricks secrets list-scopes

Oder für Mounten eines Azure Data Lake Storage Gen2 könnt ihr als Secret Scope eure Azure SubscriptionID hinterlegen, also immer dann wenn
man nicht hardcodiert Zugangsdaten im Python-Code haben will Secret Scope verwenden.
