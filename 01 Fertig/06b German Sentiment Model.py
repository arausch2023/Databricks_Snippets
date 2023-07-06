# Databricks notebook source
# MAGIC %md
# MAGIC
# MAGIC # German Sentiment Model
# MAGIC
# MAGIC https://huggingface.co/oliverguhr/german-sentiment-bert
# MAGIC
# MAGIC The model uses the Googles Bert architecture and was trained on 1.834 million German-language samples. The training data contains texts from various domains like Twitter, Facebook and movie, app and hotel reviews. 

# COMMAND ----------

pip install germansentiment

# COMMAND ----------

from germansentiment import SentimentModel

model = SentimentModel()

texts = [
    "Mit keinem guten Ergebniss",
    "Das ist gar nicht mal so gut",
    "Total awesome!",
    "nicht so schlecht wie erwartet",
    "Der Test verlief positiv.",
    "Sie fährt ein grünes Auto."]
       
result = model.predict_sentiment(texts)
print(result)

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC # Output class probabilities 

# COMMAND ----------

from germansentiment import SentimentModel

model = SentimentModel()

classes, probabilities = model.predict_sentiment(["das ist super"], output_probabilities = True) 
print(classes, probabilities)
