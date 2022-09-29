from flask import Flask
import pandas as pd
import dropbox
import os
app = Flask(__name__)

@app.route('/')
def hello_world():
    arr = os.listdir()
    print(arr)
    return 'Hello'


if __name__ == "__main__":
    app.run(debug=True, port=10000)
