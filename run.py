import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>hello there</h1>"

app.run(host=os.getenv('IP'), port=init(os.getenv('PORT')), debug=True)     