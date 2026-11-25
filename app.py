from flask import Flask
import os
app = Flask(_name_)
@app.route("/")
def home():
  version = os.getenv("APP_VERSION","v1.0")
  return f"<h1>Hello Students! Running Container Build:
  {version}</h1>"
  if_name_=="_main_":
  app.run(host="0.0.0.0",port=5001)
