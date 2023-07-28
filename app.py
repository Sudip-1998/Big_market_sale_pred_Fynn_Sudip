from flask import Flask, render_template, request
import joblib
import os
import numpy as np

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("home.html")

 
if __name__ == "__main__":
    app.run(debug=True, port=9457)
