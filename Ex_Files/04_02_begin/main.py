from flask import Flask
from distutils.log import debug

app = Flask(__name__)

@app.route("/")
def hello():
  return "Hello, World!"

app.run(debug=True)