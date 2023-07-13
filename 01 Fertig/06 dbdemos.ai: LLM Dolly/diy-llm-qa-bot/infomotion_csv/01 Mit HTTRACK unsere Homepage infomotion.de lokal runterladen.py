# Databricks notebook source
# MAGIC %md
# MAGIC
# MAGIC ## HTTRACK (Website Copier) installieren:
# MAGIC ## https://www.httrack.com/
# MAGIC
# MAGIC ## In HTTRACK als URL setzen:
# MAGIC ## https://www.infomotion.de/
# MAGIC ## Folgende Optionen setzen unter "Set Options"->"Scan Rules":
# MAGIC ## -*.png -*.gif -*.jpg -*.jpeg -*.pdf -*.mp4  -*.css -*.js -ad.doubleclick.net/* -mime:application/foobar
# MAGIC ## Damit werden keine Bilder wie *.png, *.jpeg und auch keine pdfs oder mp4s heruntergeladen
# MAGIC ## Resultat sind dann 40 MB, ca. 940 htmls lokal gespeichert, komplette Webseite 
